"""
Remote Simulation via SSH using Paramiko
Handles file transfer, remote execution, and result retrieval
"""

import paramiko
import getpass
from pathlib import Path
import sys

class RemoteSimulator:
    """Execute simulations on remote server via SSH"""
    
    def __init__(self, config_file='config/simulation_config.py'):
        """Initialize remote simulator with config"""
        # Load config
        import importlib.util
        spec = importlib.util.spec_from_file_location("config", config_file)
        config_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config_module)
        
        self.config = config_module.REMOTE_SIMULATOR
        self.sim_settings = config_module.SIMULATION_SETTINGS
        
        self.ssh = None
        self.sftp = None
        self.connected = False
        
    def connect(self):
        """Establish SSH connection using Paramiko"""
        print(f"🔐 Connecting to {self.config['username']}@{self.config['host']}...")
        
        try:
            # Get password
            password = getpass.getpass(f"Password for {self.config['username']}@{self.config['host']}: ")
            
            # Create SSH client
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            # Connect
            self.ssh.connect(
                hostname=self.config['host'],
                username=self.config['username'],
                password=password,
                port=self.config['port'],
                timeout=15
            )
            
            # Test connection
            stdin, stdout, stderr = self.ssh.exec_command('echo connected')
            output = stdout.read().decode().strip()
            
            if output == 'connected':
                print("✅ Connected successfully!")
                self.sftp = self.ssh.open_sftp()
                self.connected = True
                return True
            else:
                print("❌ Connection test failed")
                return False
                
        except paramiko.AuthenticationException:
            print("❌ Authentication failed - check username/password")
            return False
        except paramiko.SSHException as e:
            print(f"❌ SSH error: {e}")
            return False
        except Exception as e:
            print(f"❌ Connection error: {e}")
            return False
    
    def exec_command(self, command):
        """Execute a command on remote server"""
        if not self.connected:
            print("❌ Not connected to server")
            return None, None, -1
        
        try:
            stdin, stdout, stderr = self.ssh.exec_command(command, timeout=60)
            out = stdout.read().decode()
            err = stderr.read().decode()
            exit_code = stdout.channel.recv_exit_status()
            return out, err, exit_code
        except Exception as e:
            print(f"❌ Command execution error: {e}")
            return None, str(e), -1
    
    def transfer_file(self, local_file, remote_dir):
        """Transfer a file to remote server using SFTP"""
        if not self.connected:
            print("❌ Not connected to server")
            return False
        
        try:
            # Create remote directory
            self.exec_command(f"mkdir -p {remote_dir}")
            
            # Transfer file
            remote_file = f"{remote_dir}/{Path(local_file).name}"
            print(f"📤 Transferring {Path(local_file).name}...", end='')
            
            self.sftp.put(local_file, remote_file)
            print(" ✓")
            return True
            
        except Exception as e:
            print(f" ✗ ({str(e)[:50]})")
            return False
    
    def compile_module(self, module_file, remote_dir):
        """Compile a module on remote server"""
        if not self.connected:
            print("❌ Not connected to server")
            return False, "Not connected"
        
        print(f"🔧 Compiling {Path(module_file).name}...", end='')
        
        # Build compilation command
        if self.config.get('cad_setup_command'):
            setup_cmd = self.config['cad_setup_command'] + " && "
        else:
            setup_cmd = ""
        
        compile_cmd = f"""
cd {remote_dir}
{setup_cmd}{self.config['questasim_path']} -c -do "vlog {Path(module_file).name}; quit"
"""
        
        try:
            stdout, stderr, exit_code = self.exec_command(compile_cmd)
            
            if stdout is None:
                print(" ❌ Command failed")
                return False, stderr
            
            output = stdout + stderr
            
            # Check for errors
            if "Error:" in output or "** Error" in output:
                print(" ❌")
                return False, output
            else:
                print(" ✅")
                return True, output
                
        except Exception as e:
            print(f" ❌ {e}")
            return False, str(e)
    
    def cleanup(self, remote_dir):
        """Clean up remote directory"""
        if self.config.get('cleanup_remote_after_sim', False):
            print("🧹 Cleaning up remote files...")
            if self.connected:
                self.exec_command(f"rm -rf {remote_dir}")
    
    def disconnect(self):
        """Close SSH connection"""
        if self.sftp:
            self.sftp.close()
        if self.ssh:
            self.ssh.close()
        self.connected = False
        print("✅ Disconnected from server")
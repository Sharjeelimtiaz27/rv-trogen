#!/usr/bin/env python3
"""
Interactive setup wizard for simulation configuration
Handles university CAD environment systems
"""

import subprocess
from pathlib import Path

def main():
    print("="*70)
    print("🔧 RV-TROGEN SIMULATION SETUP WIZARD")
    print("="*70)
    print()
    
    # Step 1: Detect local simulators
    print("📋 STEP 1: Checking local simulator availability...")
    print()
    
    local_verilator = check_tool("verilator --version")
    local_questasim = check_tool("vsim -version")
    local_icarus = check_tool("iverilog -v")
    
    has_local = local_verilator or local_questasim or local_icarus
    
    if has_local:
        print("✅ Found local simulator(s):")
        if local_verilator: print("   - Verilator")
        if local_questasim: print("   - QuestaSim")
        if local_icarus: print("   - Icarus Verilog")
    else:
        print("❌ No local simulators found")
    
    print()
    
    # Step 2: Remote server configuration
    print("📋 STEP 2: Remote Server Configuration")
    print()
    
    use_remote = input("Do you have access to a remote server with QuestaSim? (yes/no): ").lower().strip()
    
    remote_config = {}
    if use_remote == 'yes':
        print()
        print("🔐 Remote Server Details:")
        print()
        
        remote_config['enabled'] = True
        remote_config['host'] = input("  Server hostname or IP: ").strip()
        remote_config['username'] = input("  Username: ").strip()
        
        print()
        print("🛠️  CAD Environment Setup:")
        print()
        print("Does your server use a CAD environment manager?")
        print("(e.g., you run 'cad' or 'module load' before using tools)")
        print()
        
        uses_cad_env = input("Use CAD environment manager? (yes/no) [yes]: ").lower().strip()
        uses_cad_env = uses_cad_env if uses_cad_env else "yes"
        
        if uses_cad_env == 'yes':
            print()
            print("📝 CAD Environment Setup Commands:")
            print()
            print("Example commands to run before simulation:")
            print("  - 'cad' then select option")
            print("  - 'module load questasim'")
            print("  - 'source /path/to/setup.sh'")
            print()
            
            cad_setup = input("  Enter setup command (e.g., 'cad' or 'module load questasim'): ").strip()
            
            if cad_setup == 'cad':
                print()
                print("Which CAD option to select?")
                print("  Example: '2' for Mentor Graphics")
                print("           '2.4' for Siemens 2025")
                cad_option = input("  CAD option number: ").strip()
                
                # Build the command: echo "2" | cad
                remote_config['cad_setup_command'] = f"echo '{cad_option}' | cad"
            else:
                remote_config['cad_setup_command'] = cad_setup
            
            print()
            print("After loading CAD environment, what's the QuestaSim command?")
            remote_config['questasim_path'] = input("  QuestaSim command [vsim]: ").strip() or "vsim"
        else:
            remote_config['cad_setup_command'] = None
            print()
            print("Enter full path to QuestaSim (e.g., /opt/questasim/bin/vsim)")
            remote_config['questasim_path'] = input("  QuestaSim path: ").strip()
        
        print()
        print("🔑 Authentication:")
        print("  Password authentication (prompted at runtime)")
        
        remote_config['use_ssh_key'] = False
        remote_config['ssh_key_path'] = None
        remote_config['port'] = 22
        
        print()
        remote_config['remote_work_dir'] = input("  Working directory [~/rv-trogen-sims]: ").strip() or "~/rv-trogen-sims"
        remote_config['tool'] = 'questasim'
        remote_config['transfer_method'] = 'scp'
        remote_config['cleanup_remote_after_sim'] = False
        
        print()
        print("✅ Configuration complete!")
        print(f"   Server: {remote_config['username']}@{remote_config['host']}")
        if remote_config.get('cad_setup_command'):
            print(f"   CAD setup: {remote_config['cad_setup_command']}")
        print(f"   Simulator: {remote_config['questasim_path']}")
    else:
        remote_config = {
            'enabled': False,
            'host': '',
            'username': '',
            'port': 22,
            'tool': 'questasim',
            'questasim_path': 'vsim',
            'cad_setup_command': None,
            'remote_work_dir': '~/rv-trogen-sims',
            'use_ssh_key': False,
            'ssh_key_path': None,
            'transfer_method': 'scp',
            'cleanup_remote_after_sim': False,
        }
    
    # Step 3: Choose mode
    print()
    print("📋 STEP 3: Simulation Mode")
    print()
    
    if has_local and remote_config['enabled']:
        print("You have both local and remote simulators!")
        print("  1. Auto")
        print("  2. Always local")
        print("  3. Always remote (recommended for university server)")
        mode_choice = input("Choose (1/2/3) [3]: ").strip() or "3"
        mode_map = {'1': 'auto', '2': 'local', '3': 'remote'}
        mode = mode_map.get(mode_choice, 'remote')
    elif has_local:
        mode = 'local'
        print("Using local simulator")
    elif remote_config['enabled']:
        mode = 'remote'
        print("Using remote simulator")
    else:
        print("⚠️  No simulators configured!")
        mode = 'auto'
    
    local_config = {
        'enabled': has_local,
        'tool': 'verilator' if local_verilator else ('questasim' if local_questasim else 'icarus'),
        'verilator_path': 'verilator',
        'questasim_path': 'vsim',
        'icarus_path': 'iverilog',
    }
    
    # Generate config
    print()
    print("💾 Generating configuration...")
    
    config_content = generate_config_file(mode, local_config, remote_config)
    
    config_dir = Path('config')
    config_dir.mkdir(exist_ok=True)
    
    config_file = config_dir / 'simulation_config.py'
    with open(config_file, 'w') as f:
        f.write(config_content)
    
    init_file = config_dir / '__init__.py'
    init_file.touch()
    
    print(f"✅ Saved: {config_file}")
    print()
    
    # Summary
    print("="*70)
    print("✅ SETUP COMPLETE!")
    print("="*70)
    print()
    print("Configuration:")
    print(f"  Mode: {mode}")
    if remote_config['enabled']:
        print(f"  Server: {remote_config['username']}@{remote_config['host']}")
        if remote_config.get('cad_setup_command'):
            print(f"  CAD setup: {remote_config['cad_setup_command']}")
    print()
    print("Next steps:")
    print("  1. python scripts/validate_compilation.py")
    print("  2. python scripts/run_simulations.py")
    print()


def check_tool(command):
    """Check if tool is available"""
    try:
        subprocess.run(command, shell=True, capture_output=True, timeout=5, check=False)
        return True
    except:
        return False


def generate_config_file(mode, local_config, remote_config):
    """Generate config file"""
    
    cad_command = remote_config.get('cad_setup_command', None)
    cad_command_str = f"'{cad_command}'" if cad_command else 'None'
    
    template = f'''"""
RV-TroGen Simulation Configuration

Server: {remote_config['username']}@{remote_config['host']}
CAD Setup: {cad_command}
Simulator: {remote_config['questasim_path']}
"""

# ============================================================================
# SIMULATION MODE
# ============================================================================
SIMULATION_MODE = '{mode}'

# ============================================================================
# LOCAL SIMULATOR
# ============================================================================
LOCAL_SIMULATOR = {{
    'enabled': {local_config['enabled']},
    'tool': '{local_config['tool']}',
    'verilator_path': '{local_config['verilator_path']}',
    'questasim_path': '{local_config['questasim_path']}',
    'icarus_path': '{local_config['icarus_path']}',
}}

# ============================================================================
# REMOTE SIMULATOR (University Server)
# ============================================================================
REMOTE_SIMULATOR = {{
    'enabled': {remote_config['enabled']},
    
    # Server
    'host': '{remote_config['host']}',
    'username': '{remote_config['username']}',
    'port': 22,
    
    # Authentication
    'use_ssh_key': False,
    'ssh_key_path': None,
    
    # CAD Environment Setup
    # Command to run before using simulator (e.g., 'cad' menu)
    'cad_setup_command': {cad_command_str},
    
    # Simulator
    'tool': 'questasim',
    'questasim_path': '{remote_config['questasim_path']}',
    'remote_work_dir': '{remote_config['remote_work_dir']}',
    
    # Transfer
    'transfer_method': 'scp',
    'cleanup_remote_after_sim': False,
}}

# ============================================================================
# SIMULATION SETTINGS
# ============================================================================
SIMULATION_SETTINGS = {{
    'default_cycles': 1000,
    'generate_vcd': True,
    'verbose': True,
    'parallel_sims': 1,
    'timeout_seconds': 300,
}}

# ============================================================================
# VALIDATION
# ============================================================================
VALIDATION = {{
    'compile_only': False,
    'stop_on_first_error': False,
    'generate_reports': True,
}}
'''
    
    return template


if __name__ == "__main__":
    main()
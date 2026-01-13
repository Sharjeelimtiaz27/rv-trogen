"""
RV-TroGen Simulation Configuration

Server: sharjeel@ekleer.pld.ttu.ee
CAD Setup: 2.4
Simulator: qsim
"""

# ============================================================================
# SIMULATION MODE
# ============================================================================
SIMULATION_MODE = 'remote'

# ============================================================================
# LOCAL SIMULATOR
# ============================================================================
LOCAL_SIMULATOR = {
    'enabled': True,
    'tool': 'verilator',
    'verilator_path': 'verilator',
    'questasim_path': 'vsim',
    'icarus_path': 'iverilog',
}

# ============================================================================
# REMOTE SIMULATOR (University Server)
# ============================================================================
REMOTE_SIMULATOR = {
    'enabled': True,
    
    # Server
    'host': 'ekleer.pld.ttu.ee',
    'username': 'sharjeel',
    'port': 22,
    
    # Authentication
    'use_ssh_key': False,
    'ssh_key_path': None,
    
    # CAD Environment Setup
    # Command to run before using simulator (e.g., 'cad' menu)
    'cad_setup_command': "echo '2.4' | cad",
    
    # Simulator
    'tool': 'questasim',
    'questasim_path': 'vsim',
    'remote_work_dir': '/home/sharjeel/sharjeelphd/Research/rv_trogen',
    
    # Transfer
    'transfer_method': 'scp',
    'cleanup_remote_after_sim': False,
}

# ============================================================================
# SIMULATION SETTINGS
# ============================================================================
SIMULATION_SETTINGS = {
    'default_cycles': 1000,
    'generate_vcd': True,
    'verbose': True,
    'parallel_sims': 1,
    'timeout_seconds': 300,
}

# ============================================================================
# VALIDATION
# ============================================================================
VALIDATION = {
    'compile_only': False,
    'stop_on_first_error': False,
    'generate_reports': True,
}

import importlib

def get_experiment(name):
    module = importlib.import_module(f'GRL_Experiment.Exp_EmergencyVehicle.{name}')
    return module

experiments = {
    'A2C': 'EV_A2C',
    'AC': 'EV_AC',
    'DDPG': 'EV_DDPG',
    'DoubleNAF': 'EV_DoubleNAF',
    'NAF': 'EV_NAF',
    'PPO': 'EV_PPO',
    'REINFORCE': 'EV_REINFORCE',
    'TD3': 'EV_TD3',
}

def load_experiment(name):
    if name in experiments:
        return get_experiment(experiments[name])
    else:
        raise ValueError(f"Experiment {name} not found")

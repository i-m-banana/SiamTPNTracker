from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.
    settings.got10k_path = r'E:\pycharm_work\data\GOT-10k\val_data'
    settings.save_dir = './results/'
    settings.got_packed_results_path = './results/'
    settings.got_reports_path = './results/'
    settings.lasot_path = ''
    settings.otb_path = ''
    settings.result_plot_path = './results/result_plots/'
    settings.results_path = './results/tracking_results' 
    settings.trackingnet_path = ''
    settings.uav_path =''
    settings.vot_path = ''

    return settings


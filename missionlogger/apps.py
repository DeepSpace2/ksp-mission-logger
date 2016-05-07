from django.apps import AppConfig
from django.conf import settings
import os


class MissionloggerConfig(AppConfig):
    name = 'missionlogger'

    def get_all_vessels(self, ksp_root_path):
        def get_all_vessels_names_in_path(path):
            return [f.split('.')[0] for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

        all_vessels_names = []

        for dirpath, *_ in os.walk(ksp_root_path):
            if '@thumbs' not in dirpath and ('SPH' in dirpath or 'VAB' in dirpath):
                all_vessels_names.extend(get_all_vessels_names_in_path(dirpath))

        return sorted(set(all_vessels_names))

    def ready(self):
        vessel_model = self.get_model('Vessel')
        all_vessels = self.get_all_vessels(settings.ROOT_KSP_PATH)
        for vessel_name in all_vessels:
            try:
                vessel_model.objects.get(name=vessel_name)
            except vessel_model.DoesNotExist:
                vessel_model(name=vessel_name).save()

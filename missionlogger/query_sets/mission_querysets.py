from missionlogger.models import Mission


def get_all_missions():
    return Mission.objects.all()


def get_mission_by_id(pk):
    return Mission.objects.get(pk=pk)


def get_missions_by_vessel(vessel):
    return Mission.objects.filter(vessel__name=vessel)


def get_missions_by_mission_status(mission_status):
    return Mission.objects.filter(status=mission_status)

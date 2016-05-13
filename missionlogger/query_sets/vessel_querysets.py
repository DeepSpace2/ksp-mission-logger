from missionlogger.models import Vessel


def get_all_vessels(order_by=None):
    vessels = Vessel.objects.all()
    if order_by:
        vessels = vessels.order_by(order_by)
    return vessels

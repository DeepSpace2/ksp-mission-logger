from django import forms
from django.shortcuts import render
from django.views.generic import View, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Mission, Vessel
from .query_sets import mission_querysets, vessel_querysets


class Index(View):
    def get(self, request, vessel_name=None, mission_status=None):
        if not vessel_name and not mission_status:
            context = {'object_list': mission_querysets.get_all_missions()}
        elif vessel_name:
            context = {'object_list': mission_querysets.get_missions_by_vessel(vessel_name)}
        else:
            context = {'object_list': mission_querysets.get_missions_by_mission_status(mission_status)}
        return render(request, 'missionlogger/index.html', context=context, status=200)


class VesselCreate(CreateView):
    model = Vessel
    fields = ['name']


class MissionDetail(View):
    def get(self, request, mission_id):
        context = {'mission': mission_querysets.get_mission_by_id(mission_id)}
        return render(request, 'missionlogger/mission_detail.html', context=context)


class MissionForm(forms.ModelForm):
    vessel = forms.ModelChoiceField(queryset=vessel_querysets.get_all_vessels(order_by='name'))

    class Meta:
        model = Mission
        fields = ['title', 'vessel', 'status', 'details']


class MissionCreate(CreateView):
    form_class = MissionForm
    model = Mission


class MissionUpdate(UpdateView):
    form_class = MissionForm
    model = Mission


class MissionDelete(DeleteView):
    model = Mission
    success_url = reverse_lazy('missionlogger:index')


class AllVessels(View):
    def get(self, request):
        return render(request, 'missionlogger/vessels.html',
                      context={'vessels': vessel_querysets.get_all_vessels('name')},
                      status=200)

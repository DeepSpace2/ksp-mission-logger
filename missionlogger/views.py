from django import forms
from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Mission, Vessel
from .query_sets import mission_querysets


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
    # TODO change to show proper info
    def get(self, request, mission_id):
        context = {'mission': Mission.objects.get(pk=mission_id)}
        return render(request, 'missionlogger/mission_detail.html', context=context)


class MissionForm(forms.ModelForm):
    vessel = forms.ModelChoiceField(queryset=Vessel.objects.all().order_by('name'))

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

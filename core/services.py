from django.http import Http404

from core import models, serializers


def get_model_instance_by_id(pk: int, model):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise Http404


def put_info_to_user_profile(user_id: int, data: dict):
    serializer = serializers.SeatQuestSerializer(
        get_model_instance_by_id(pk=user_id, model=models.CustomUser),
        data=data,
        partial=True
    )
    if serializer.is_valid():
        serializer.save()
        return [True, serializer.data]
    return [False, serializer.errors]

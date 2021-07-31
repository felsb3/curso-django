from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Video Aperitivo: Motivação', 'youtube_id': 'ipgrkrNCBzA'}
    return render(request, 'aperitivos/video.html', context={'video': video})
# videos = zLIeu9cPYrY
# titulo = Como publicar um site Django em MENOS DE 30 MINUTOS — Imersão Django (EP. 1)
# videos = ipgrkrNCBzA
# titulo = JORNADA RUMO A PRIMEIRA VAGA!
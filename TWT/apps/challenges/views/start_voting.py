from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from ..models import Challenge
from TWT.context import get_discord_context
from TWT.discord import client


class StartVoting(View):
    def get_context(self, request: WSGIRequest) -> dict:
        return get_discord_context(request=request)

    def get(self, request: WSGIRequest, challenge_id: int):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.INFO, "You are not logged in!")
            return redirect("/")

        context = self.get_context(request=request)
        if not context["is_verified"]:
            return redirect("/")
        if context["is_admin"] or context["is_challenge_host"]:
            challenge = get_object_or_404(
                Challenge, id=challenge_id
            )  # Challenge.objects.get(id=challenge_id)
            if challenge.team_creation_status or challenge.submissions_status:
                messages.add_message(
                    request, messages.WARNING, "Stop Team creation or Submission first"
                )
                return redirect("timathon:Home")
            challenge.voting_status = True
            challenge.save()
            messages.add_message(
                request,
                messages.INFO,
                "Voting has been started Go vote now for your favourite projects",
            )
            client.send_webhook(
                "Timathon",
                f"Voting period has been started",
                fields=[
                    {
                        "name": "Link",
                        "value": f"[Visit]({request.build_absolute_uri('/timathon/')})",
                    }
                ],
                codeJamInfo=True,
            )
            client.send_webhook(
                "Code Jam",
                f"<@{context['discord_user'].uid}> has started the Voting period",
                fields=[
                    {
                        "name": "Link",
                        "value": f"[Visit]({request.build_absolute_uri('/timathon/')})",
                    }
                ],
            )
            return redirect("timathon:Home")

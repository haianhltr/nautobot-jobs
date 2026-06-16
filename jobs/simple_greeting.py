"""Simple Greeting Form — example Job loaded from Git."""

from nautobot.apps import jobs

name = "My GitHub Jobs"


class SimpleGreetingJob(jobs.Job):
    class Meta:
        name = "Simple Greeting Form"
        description = "Greeting Job sourced from the nautobot-jobs Git repository."
        has_sensitive_variables = False

    person_name = jobs.StringVar(
        label="Your name",
        description="Who should we greet?",
        default="world",
    )

    message = jobs.TextVar(
        label="Message",
        description="Optional note to include in the job output.",
        required=False,
        default="Thanks for trying Nautobot Jobs from Git!",
    )

    mood = jobs.ChoiceVar(
        choices=(
            ("happy", "Happy"),
            ("excited", "Excited"),
            ("calm", "Calm"),
        ),
        description="Pick a mood for the greeting.",
        default="happy",
    )

    def run(self, *, person_name, message, mood):
        self.logger.info("Hello, %s! (feeling %s)", person_name, mood)
        if message:
            self.logger.info("Message: %s", message)
        self.logger.success("Done! Job ran from Git repository.")


jobs.register_jobs(SimpleGreetingJob)

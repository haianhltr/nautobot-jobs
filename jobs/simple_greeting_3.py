"""Simple Greeting Form 3 — Job on the demo-greeting-3 Git branch."""

from nautobot.apps import jobs

name = "My GitHub Jobs"


class SimpleGreetingForm3Job(jobs.Job):
    class Meta:
        name = "Simple Greeting Form 3"
        description = "Greeting Job from the demo-greeting-3 branch of nautobot-jobs."
        has_sensitive_variables = False

    person_name = jobs.StringVar(
        label="Your name",
        description="Who should we greet?",
        default="branch tester",
    )

    message = jobs.TextVar(
        label="Message",
        description="Optional note to include in the job output.",
        required=False,
        default="Synced from the demo-greeting-3 branch!",
    )

    mood = jobs.ChoiceVar(
        choices=(
            ("happy", "Happy"),
            ("excited", "Excited"),
            ("calm", "Calm"),
        ),
        description="Pick a mood for the greeting.",
        default="calm",
    )

    def run(self, *, person_name, message, mood):
        self.logger.info("Greeting #3 (branch demo-greeting-3) for %s (feeling %s)", person_name, mood)
        if message:
            self.logger.info("Message: %s", message)
        self.logger.info("Simple Greeting Form 3 completed.")


jobs.register_jobs(SimpleGreetingForm3Job)

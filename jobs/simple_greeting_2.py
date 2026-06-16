"""Simple Greeting Form 2 — second example Job from Git."""

from nautobot.apps import jobs

name = "My GitHub Jobs"


class SimpleGreetingForm2Job(jobs.Job):
    class Meta:
        name = "Simple Greeting Form 2"
        description = "Second greeting Job from the nautobot-jobs Git repository."
        has_sensitive_variables = False

    person_name = jobs.StringVar(
        label="Your name",
        description="Who should we greet?",
        default="friend",
    )

    message = jobs.TextVar(
        label="Message",
        description="Optional note to include in the job output.",
        required=False,
        default="Hello again from Git!",
    )

    mood = jobs.ChoiceVar(
        choices=(
            ("happy", "Happy"),
            ("excited", "Excited"),
            ("calm", "Calm"),
        ),
        description="Pick a mood for the greeting.",
        default="excited",
    )

    def run(self, *, person_name, message, mood):
        self.logger.info("Greeting #2 for %s (feeling %s)", person_name, mood)
        if message:
            self.logger.info("Message: %s", message)
        self.logger.success("Simple Greeting Form 2 completed.")


jobs.register_jobs(SimpleGreetingForm2Job)

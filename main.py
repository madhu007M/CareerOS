from rich.console import Console

from scripts.core.collector_manager import CollectorManager
from scripts.collectors.mock.mock_collector import MockCollector

console = Console()


def main():

    console.rule("[bold cyan]CareerOS[/bold cyan]")

    manager = CollectorManager()

    manager.register(MockCollector())

    for collector in manager.get_collectors():

        console.print(f"\n[bold yellow]Running {collector.name}[/bold yellow]")

        jobs = collector.search_jobs(
            keyword="Cyber Security",
            location="India"
        )

        for job in jobs:

            console.print(
                f"[green]✓[/green] "
                f"{job['company']} | "
                f"{job['role']} | "
                f"{job['location']}"
            )


if __name__ == "__main__":
    main()
import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument('task')
def add(task):
    """Add a new task."""
    # Write code to add the task to the todo list
    click.echo(f'Task "{task}" added.')


@cli.command()
def list():
    """List all tasks."""
    # Write code to retrieve and display the list of tasks
    click.echo('List of tasks:')
    # Replace the line below with code to iterate over tasks and print them
    click.echo('Task 1')
    click.echo('Task 2')


@cli.command()
@click.argument('task_id', type=int)
def complete(task_id):
    """Mark a task as completed."""
    # Write code to mark the task as completed
    click.echo(f'Task {task_id} marked as completed.')


@cli.command()
@click.argument('task_id', type=int)
def delete(task_id):
    """Delete a task."""
    # Write code to delete the task
    click.echo(f'Task {task_id} deleted.')


if __name__ == '__main__':
    cli()

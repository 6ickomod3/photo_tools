import click
import os
from photo_tools.timelapse import create_timelapse as make_timelapse

@click.group()
def cli():
    """Photo Tools CLI - A tool for processing photos and videos."""
    pass

@cli.command()
@click.option('--input-dir', '-i', required=True, type=click.Path(exists=True), help='Input directory containing images.')
@click.option('--output', '-o', default='output.mp4', help='Output video filename.')
@click.option('--fps', '-f', default=30, help='Frames per second.')
@click.option('--ext', '-e', default='*.jpg', help='Image file extension pattern (e.g., *.png).')
@click.option('--resolution', '-r', help='Target resolution (e.g., 1920x1080) or scale factor (e.g., 0.5).')
def timelapse(input_dir, output, fps, ext, resolution):
    """Create a time-lapse video from a folder of images."""
    click.echo(f"Starting time-lapse creation from {input_dir}...")
    make_timelapse(input_dir, output, fps, ext, resolution)

if __name__ == '__main__':
    cli()

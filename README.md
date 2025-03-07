# napari-animation

[![License](https://img.shields.io/pypi/l/napari-animation.svg?color=green)](https://github.com/napari/napari-animation/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-animation.svg?color=green)](https://pypi.org/project/napari-animation)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-animation.svg?color=green)](https://python.org)
[![tests](https://github.com/napari/napari-animation/actions/workflows/test_and_deploy.yml/badge.svg)](https://github.com/napari/napari-animation/actions)
[![codecov](https://codecov.io/gh/napari/napari-animation/branch/main/graph/badge.svg)](https://codecov.io/gh/napari/napari-animation)

**napari-animation** is a plugin for making animations in [napari].

<p align="center">
  <img width="500" src="https://user-images.githubusercontent.com/7307488/196110138-6c4663b1-67b2-4c79-97b7-57b706d1d49c.gif">
</p>

----------------------------------

[Merlin Lange](https://twitter.com/Merlin_Lange) used *napari-animation* to create one of [Nature's best science images for September 2022](https://www.nature.com/immersive/d41586-022-03051-6/index.html)

----------------------------------

This plugin is built on [naparimovie](https://github.com/guiwitz/naparimovie) from @guiwitz. naparimovie was submitted to napari in [PR#851](https://github.com/napari/napari/pull/780) before napari plugin infrastructure existed.

----------------------------------
## Overview

**napari-animation** provides a framework for the creation of animations in napari, the plugin contains:
- an easy to use GUI for creating animations interactively
- a Python package for the programmatic creation of animations

This plugin remains under development and contributions are very welcome, please open an issue to discuss potential improvements.

## Installation

### PyPI
`napari-animation` is available through the Python package index and can be installed using `pip`.

```sh
pip install napari-animation
```

> [!WARNING]
> `napari-animation` uses `ffmpeg` to export animations. If you are using a macOS arm64 computer (Apple Silicon e.g. M1, M2 processor)
> the PyPI package does not include the needed binary for your platform. You will need to install `ffmpeg` using
> `conda` from the [conda-forge channel](https://conda-forge.org/docs/#what-is-conda-forge) (`conda install -c conda-forge ffmpeg`)
> or using [`homebrew`](https://brew.sh) (`brew install ffmpeg`).

### Conda
`napari-animation` is also available for install using `conda` through the [conda-forge channel](https://conda-forge.org/docs/#what-is-conda-forge).

```sh
conda install -c conda-forge napari-animation
```

### Local
You can clone this repository and install locally with

    pip install -e .

### Interactive use
**napari-animation** can be used interactively.

An animation is created by capturing [keyframes](https://en.wikipedia.org/wiki/Key_frame) containing the current viewer state.

<p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/7307488/196113682-96ce0da3-fa5c-411e-8fb1-52dc3a8f96b6.png">
</p>

To activate the GUI, select **napari-animation: wizard** from the *plugins menu*

<p align="center">
  <img width="200" src="https://user-images.githubusercontent.com/7307488/196114466-56cb5985-0d79-4cfa-96f1-38cf3ccfbc48.png">
</p>

### Headless
**napari-animation** can also be run headless, allowing for reproducible, scripted creation of animations.

```python
from napari_animation import Animation

animation = Animation(viewer)

viewer.dims.ndisplay = 3
viewer.camera.angles = (0.0, 0.0, 90.0)
animation.capture_keyframe()
viewer.camera.zoom = 2.4
animation.capture_keyframe()
viewer.camera.angles = (-7.0, 15.7, 62.4)
animation.capture_keyframe(steps=60)
viewer.camera.angles = (2.0, -24.4, -36.7)
animation.capture_keyframe(steps=60)
viewer.reset_view()
viewer.camera.angles = (0.0, 0.0, 90.0)
animation.capture_keyframe()
animation.animate('demo.mov', canvas_only=False)
```

## Examples
Examples can be found in our [examples](examples) folder. Simple examples for both interactive and headless 
use of the plugin follow.

## Contributing

Contributions are very welcome and a detailed contributing guide is coming soon.
In the meantime, clone this repository and install it in editable mode using `pip`. 
We recommend using a virtual environment, for example `conda`.
> [!IMPORTANT]
> Ensure you have a suitable Qt backend for napari! We recommend `PyQt5`.
> For more information, see the napari [Qt backend installation guide](https://napari.org/stable/tutorials/fundamentals/installation.html#choosing-a-different-qt-backend)

```sh
conda create -n nap-anim python=3.10
conda activate nap-anim
pip install -e ".[dev]" PyQt5

```

Tests are run with `pytest`.
You can make sure your `[dev]` installation is working properly by running
`pytest .` from within the repository.

> [!NOTE]
> We use [`pre-commit`](https://pre-commit.com) to sort imports and lint with
> [`ruff`](https://github.com/astral-sh/ruff) and format code with
> [`black`](https://github.com/psf/black) automatically prior to each commit.
> To minmize test errors when submitting pull requests, please install `pre-commit`
> in your environment as follows:
> ```sh
> pre-commit install
> ```

## License

Distributed under the terms of the [BSD-3] license,
"napari-animation" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin
[file an issue]: https://github.com/sofroniewn/napari-animation/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/

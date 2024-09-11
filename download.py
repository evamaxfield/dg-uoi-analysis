from pathlib import Path
from shutil import unpack_archive, rmtree

import gdown
import typer

###############################################################################
# Constants

PARENT_DIR = Path(__file__).resolve().parent
DATA_DIR = PARENT_DIR / "data"
ARCHIVES_DIR = PARENT_DIR / "archives"
PER_DAY_PKG_RELEASES_METRICS_ONE_YEAR_GID = "1jJ7onjoQeugY4yEo9PMl34MccCrClOrZ"
PER_DAY_PKG_RELEASES_METRICS_TWO_YEAR_GID = "1u81adayYdre5O6eBnP69Bv-iDHMDO92-"
PER_DAY_PKG_RELEASES_METRICS_SIX_MONTHS_GID = "1TN4Gjz1RkKNT-SqG7p-zWCqGJ7gHl0-Q"
PER_DAY_RELEASE_CONTENT_METRICS_ONE_YEAR_RATED_GID = "1xIhRQEqLic2Pn0gmzZvtmydimjEfmcS0"

# Create the LUT
DATASET_NAME_TO_GID_LUT = {
    "per-day-pkg-releases-metrics-one-year": (
        PER_DAY_PKG_RELEASES_METRICS_ONE_YEAR_GID
    ),
    "per-day-pkg-releases-metrics-two-year": (
        PER_DAY_PKG_RELEASES_METRICS_TWO_YEAR_GID
    ),
    "per-day-pkg-releases-metrics-six-months": (
        PER_DAY_PKG_RELEASES_METRICS_SIX_MONTHS_GID
    ),
    "per-day-release-content-metrics-one-year-rated": (
        PER_DAY_RELEASE_CONTENT_METRICS_ONE_YEAR_RATED_GID
    ),
}

###############################################################################
# App

app = typer.Typer()

###############################################################################

@app.command()
def download_and_extract_data(
    dataset_name: str,
) -> None:
    # Check dataset name
    if dataset_name not in DATASET_NAME_TO_GID_LUT:
        raise ValueError(
            f"Dataset {dataset_name} not found. "
            f"Valid dataset names are: {list(DATASET_NAME_TO_GID_LUT.keys())}."
        )
    
    # Get dataset gid
    dataset_gid = DATASET_NAME_TO_GID_LUT[dataset_name]

    # Create data dir
    DATA_DIR.mkdir(exist_ok=True)

    # Create archives dir
    ARCHIVES_DIR.mkdir(exist_ok=True)

    # Create output path for dataset archive
    dataset_archive_path = ARCHIVES_DIR / f"{dataset_name}.tar.gz"

    # Delete existing archive if exists
    if dataset_archive_path.exists():
        print("Removing existing archive...")
        dataset_archive_path.unlink()

    # Download data
    gdown.download(
        id=dataset_gid,
        output=str(dataset_archive_path),
    )

    # Remove existing unpacked data if exists
    unpacked_data_dir = DATA_DIR / dataset_name
    if unpacked_data_dir.exists():
        print("Removing existing data...")
        rmtree(unpacked_data_dir)

    # Extract data
    unpack_archive(
        filename=str(dataset_archive_path),
        extract_dir=str(PARENT_DIR),
        format="gztar",
    )

    # Clean up any "._*" files
    print("Cleaning up extra files...")
    for p in DATA_DIR.rglob("._*"):
        p.unlink()

    # Print success message
    print(f"Data downloaded and extracted to {unpacked_data_dir}.")


###############################################################################

if __name__ == "__main__":
    app()
import os
import shutil
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.io
from termcolor import cprint


class prnt:
    """
    Prints colorful terminal messages.
    """

    @classmethod
    def err(cls, string):
        cprint("ERROR", "red", attrs=["bold"], end=" ")
        print(string)

    @classmethod
    def warn(cls, string):
        cprint("WARNING", "yellow", attrs=["bold"], end=" ")
        print(string)

    @classmethod
    def succ(cls, string):
        cprint("SUCCESS", "green", attrs=["bold"], end=" ")
        print(string)


def prepro(dataroot):
    """
    main summarizes the output of the 4afc experiment into a single csv file
    for easier analysis.

    Parameters
    ----------
    dataroot : pathlib.Path instance
        The root directory of the data

    Raises
    ------
    ValueError
        If the number of recordings for the low
        and the high condition are not the same.
    """

    # make direcories to sort data
    lowdir = Path(f"{dataroot}/low")  # name for low directory
    highdir = Path(f"{dataroot}/high")  # name for high directory

    # create temporary folders to later iterate through
    if os.path.exists(lowdir) is False:
        os.mkdir(lowdir)
    else:
        prnt.warn(
            "The directories already exist! Nothing will be done unless you delete them!")

    if os.path.exists(highdir) is False:
        os.mkdir(highdir)

    # sort the lows to low folder and highs to high folder
    for file in dataroot.iterdir():

        # move lows to lowdir
        if (file.is_file()) and ('low' in str(file)):
            _, filename = os.path.split(file)
            shutil.move(file, f"{lowdir}/{filename}")

        # move highs to highdir
        if (file.is_file()) and ('high' in str(file)):
            _, filename = os.path.split(file)
            shutil.move(file, f"{highdir}/{filename}")

    # check if number of low and high files are the same
    num_low = len(os.listdir(lowdir))
    num_high = len(os.listdir(highdir))
    if num_low != num_high:
        raise ValueError(
            "There is not the same number of 'low' and 'high' files!")

    # iterate through low and high files and put into dataframe
    d = {
        "subj": [],
        "cat": [],
        "what": [],
        "prop": [],
    }
    for i in range(num_low):

        # load low and high dataset for respective subject
        low = np.asarray(
            scipy.io.loadmat(
                f"{lowdir}/{os.listdir(lowdir)[i]}")["result_mat_low"])
        high = np.asarray(
            scipy.io.loadmat(
                f"{highdir}/{os.listdir(highdir)[i]}")["result_mat_high"])

        # get id of subject
        subj = str(os.listdir(lowdir)[i]).split("_", maxsplit=1)[0]

        # make list of categories for dataframe (low and high)
        cats = [["low" for i in range(len(low))], [
            "high" for i in range(len(high))]]
        cats = [item for sublist in cats for item in sublist]

        # make list to later convert to pandas dataframe
        d["subj"].extend([subj for i in range(len(low)*2)])
        d["cat"].extend(cats)
        d["what"].extend(np.ravel([low[:, 0], high[:, 0]]).tolist())
        d["prop"].extend(
            np.ravel([low[:, 1]/low[:, 2], high[:, 1]/high[:, 2]]).tolist())

    # convert the whole shit to a pandas dataframe
    df = pd.DataFrame(d)

    # save dataframe to csv
    df.to_csv(f"{dataroot}/4afc_all.csv")

    if os.path.exists(f"{dataroot}/4afc_all.csv"):
        prnt.succ("Output file created or exists already!")


if __name__ == "__main__":

    dataroot = Path('../data/test/4afc')  # root data directory
    prepro(dataroot)

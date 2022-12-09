import os
from pathlib import Path

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def dataimport(dataroot: str, processed_dataroot: str) -> pd.DataFrame:

    dfs = []
    for i, file in enumerate(os.listdir(dataroot)):

        path = f"{dataroot}/{file}"
        name = file.split("-")[0]

        df = pd.read_excel(path, header=None)
        df.columns = [
            "trialno",
            "correctno",
            "delay",
            "cpd",
            "selected",
            "totdur",
            "switches",
            "tpertrial",
        ]

        # add row with subject name
        df["subj"] = [name for i in range(df.shape[0])]
        df["strat_idx"] = df.tpertrial / df.switches
        df["iserror"] = np.array(df.correctno!=df.selected, dtype=int)

        dfs.append(df)

    # concatenate dfs for all subjects
    data = pd.concat(dfs, ignore_index=True)
    data.strat_idx = data.strat_idx/(data.strat_idx.max()-data.strat_idx.min())

    # save df to csv
    filename = f"{processed_dataroot}/cvs.csv"
    data.to_csv(filename)

    # load data from processed dataroot
    df = pd.read_csv(filename)

    return df


if __name__ == '__main__':
    colors = mcolors.TABLEAU_COLORS

    # import the data
    dataroot = Path("data/cvs")
    processed_dataroot = Path("data_processed")
    df = dataimport(dataroot, processed_dataroot)

    # delete JONA!
    # df = df[df.subj != 'VP1']

    # compute statistics irrespective of delay

    # means and sem for trial duration
    names = np.unique(df.subj).tolist()
    n = df.shape[1] / len(names)
    means = np.array(df.tpertrial.groupby(df.subj).mean())
    sems = np.array(df.tpertrial.groupby(df.subj).std()) / np.sqrt(n)

    # put to dataframe
    df_all = pd.DataFrame(
        list(zip(names, means, sems)),
        columns=("names", "tpertrial_means", "tpertrial_sems"),
    )

    # means and sems for no of switches
    means = np.array(df.switches.groupby(df.subj).mean())
    sems = np.array(df.switches.groupby(df.subj).std()) / np.sqrt(n)
    df_all["switches_means"] = means
    df_all["switches_sems"] = sems

    # plot data for all subjects
    for name, color in zip(df_all.names, colors):
        minidf = df_all[df_all.names == name]
        plt.errorbar(
            minidf.switches_means,
            minidf.tpertrial_means,
            xerr=minidf.switches_sems,
            yerr=minidf.tpertrial_sems,
            fmt="bo",
            label=name,
            color=color,
        )
    plt.legend()
    plt.show()

    # repeat analysis for no duration and 2 seconds duration
    df_low = df[df.delay == 0]

    # means and sem for trial duration
    names = np.unique(df_low.subj).tolist()
    n = df_low.shape[1] / len(names)
    means = np.array(df_low.tpertrial.groupby(df_low.subj).mean())
    sems = np.array(df_low.tpertrial.groupby(df_low.subj).std()) / np.sqrt(n)

    # put to dataframe
    df_all = pd.DataFrame(
        list(zip(names, means, sems)),
        columns=("names", "tpertrial_means", "tpertrial_sems"),
    )

    # means and sems for no of switches
    means = np.array(df_low.switches.groupby(df_low.subj).mean())
    sems = np.array(df_low.switches.groupby(df_low.subj).std()) / np.sqrt(n)
    df_all["switches_means"] = means
    df_all["switches_sems"] = sems

    # plot data for all subjects
    for name, color in zip(df_all.names, colors):
        minidf = df_all[df_all.names == name]
        plt.errorbar(
            minidf.switches_means,
            minidf.tpertrial_means,
            xerr=minidf.switches_sems,
            yerr=minidf.tpertrial_sems,
            label=name,
            color=color,
        )
    plt.legend()
    plt.show()

    sems_low = sems
    means_low = means


    # repeat analysis for no duration and 2 seconds duration
    df_low = df[df.delay == 1.5]

    # means and sem for trial duration
    names = np.unique(df_low.subj).tolist()
    n = df_low.shape[1] / len(names)
    means = np.array(df_low.tpertrial.groupby(df_low.subj).mean())
    sems = np.array(df_low.tpertrial.groupby(df_low.subj).std()) / np.sqrt(n)

    # put to dataframe
    df_all = pd.DataFrame(
        list(zip(names, means, sems)),
        columns=("names", "tpertrial_means", "tpertrial_sems"),
    )

    # means and sems for no of switches
    means = np.array(df_low.switches.groupby(df_low.subj).mean())
    sems = np.array(df_low.switches.groupby(df_low.subj).std()) / np.sqrt(n)
    df_all["switches_means"] = means
    df_all["switches_sems"] = sems

    # plot data for all subjects
    for name, color in zip(df_all.names, colors):
        minidf = df_all[df_all.names == name]

        print(minidf.tpertrial_sems)
        print(minidf.switches_sems)

        plt.errorbar(
            minidf.switches_means,
            minidf.tpertrial_means,
            xerr=minidf.switches_sems,
            yerr=minidf.tpertrial_sems,
            label=name,
            color=color,
        )

    plt.legend()
    plt.show()


    sems_high = sems
    means_high = means

    # for i in range(len(sems_high)):
    #     plt.errorbar(, minidf.tpertrial_means,
    #                  xerr=minidf.switches_sems, yerr=minidf.tpertrial_sems, label=name, color=color)
    #

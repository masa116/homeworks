import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

class Sake(object):
    def __init__(self, sakedata_labels):
        self.sakedata_labels = sakedata_labels
        self.sd = None

    def read_csv(self, sake_data_path):
        self.sd = pd.read_csv(sake_data_path)

    def get_col(self):
        self.sd = self.sd[self.sakedata_labels]
        self.sd = self.sd.dropna()
        self.sd = self.sd.reset_index(drop=True)

    def get_standarnised(self):
        sc = StandardScaler()
        sc.fit(self.sd)
        a = sc.transform(self.sd)
        df_tmp = pd.DataFrame(a)
        for i, s in enumerate(self.rename_label()):
            df_tmp.rename(columns={i: s}, inplace=True)
        return df_tmp

    def concat(self, df):
        self.sd = pd.concat([self.sd, df], axis=1)

    def get_standarnised_concat_sakedata(self, sake_data_path):
        self.read_csv(sake_data_path)
        self.get_col()
        df_tmp = self.get_standarnised()
        self.concat(df_tmp)

    def rename_label(self):
        label_list = []
        for s in self.sakedata_labels:
            s = 's_' + s
            label_list.append(s)
        return label_list

    def get_s_sakedata(self):
        return self.sd[self.rename_label()]

def plot_2D_scatter(df_sct, color_list, sakelabels):
    for df_tmp, color in zip(df_sct, color_list):
        plt.scatter(x=df_tmp[sakelabels[0]], y=df_tmp[sakelabels[1]], c=color)
    plt.xlabel(sakelabels[0])
    plt.ylabel(sakelabels[1])
    plt.show()

def km_cluster(sd, n):
    km = KMeans(n_clusters=n)
    km.fit(sd)
    return km.labels_

def main(sake_data_path, n, color_list, sakedata_labels):
    s = Sake(sakedata_labels)
    s.get_standarnised_concat_sakedata(sake_data_path)
    s.sd['cluster'] = km_cluster(s.get_s_sakedata(), n)
    df_sct = []
    for i in range(n):
        df_sct.append(s.sd[s.sd['cluster'] == i])
    plot_2D_scatter(df_sct, color_list, sakedata_labels)

if __name__ == '__main__':
    sake_data_path = "data/sakemonogatari/sake_data.csv"
    n_clusters = 4
    color_list = ['r', 'b', 'g', 'y']
    sakedata_labels = ['nihonsyudo', 'sando']
    main(sake_data_path, n_clusters, color_list, sakedata_labels)


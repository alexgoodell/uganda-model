

from dependencies import *

def clean_columns(df):
	df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
	return df



def hist(df, cn, num_cols, title, xlabel):
	top = df[cn].value_counts()[:num_cols].keys().tolist()
	plt.figure(figsize=(10, 5))
	g = sns.countplot(x=cn, data=df[df[cn].isin(top)], palette="Greens_d", order=top)
	_ = plt.xticks(rotation=90)
	_ = plt.xlabel(title)
	_ = plt.title(xlabel)

def tab(df, cns):
	for cn in cns:
		print "\n\n{}".format(titlecase(cn))
		print tabulate.tabulate(df[cn].value_counts(),tablefmt="pipe", headers=['Name', 'Count']) 

def pt(df):
	headers = df.columns
	return tabulate.tabulate(df,tablefmt="pipe", headers=headers)


def rename_vals(df, xs):
	for x in xs:
		df.loc[df[x['col']].isin(x['old_names']), x['col']] = x['new_name']

# required to use as module
if __name__ == '__main__': 
	print "hello world"
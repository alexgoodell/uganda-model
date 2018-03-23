

from dependencies import *


# --------------------------- Pandas / matplot lib ----------------------------
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
		print tabulate.tabulate(pd.DataFrame(df[cn].value_counts()),tablefmt="pipe", headers=['Name', 'Count']) 

def rename_vals(df, xs):
	for x in xs:
		df.loc[df[x['col']].isin(x['old_names']), x['col']] = x['new_name']

# -------------------------------- Formatting ---------------------------------

def pt(df, headers=0, title=0):
	if not isinstance(df, pd.DataFrame):
		try:
			df = pd.DataFrame(df)
		except:
			print "error cannot make pretty table"
	if headers==0 and len(df.columns.values)>1:
		headers = df.columns
		table = tabulate.tabulate(df,tablefmt="pipe", headers=headers)
	elif headers==0 and not len(df.columns)>1:
		table = tabulate.tabulate(df,tablefmt="pipe")
	else:
		table = tabulate.tabulate(df,tablefmt="pipe", headers=headers)	
	if title != 0:
		length = len(table.split('\n')[0])
		x = '{:^' + str(length) + '}'
		r = x.format(title)
		table = r + '\n\n' + table
	return "\n\n" + table


def fmt2sf(v):
	if not is_number(v):
		return v
	if v > 10000000000: # if over 10 bill, 0 decmial point
		v = v/1000000000
		return "{:,.0f}b".format(float('%.3g' % v))
	if v > 1000000000: # if over 1 bill, 1 decmial point
		v = v/1000000000
		return "{:,.1f}b".format(float('%.3g' % v))
	if v > 100000000: # if over 100 mill, two decmial points
		v = v/1000000000
		return "{:,.2f}b".format(float('%.3g' % v))
	if v > 1000000:
		v = v/100000
		return "{:,.0f}m".format(float('%.3g' % v))
	if v > 1000:
		v = v/1000
		return "{:,.0f}k".format(float('%.3g' % v))
	if v >= 10:
		return "{:,.0f}".format(float('%.3g' % v))
	else:
		return "{:.2f}".format(float('%.2g' % v))


def is_number(s):
    """ Returns True is string is a number. """
    try:
        float(s)
        return True
    except ValueError:
        return False

# ----------------------------------- Other -----------------------------------

# required to use as module
if __name__ == '__main__': 
	print "hello world"
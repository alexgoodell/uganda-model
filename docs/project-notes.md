

# Dec 27 2018, Uganda anesthesia workforce model: Initial plans


- Objective: To better understand the workforce/capacity of anesthesia services in Uganda and to assess different potential policy options for the scale-up of workforce/capacity. The project will be completed in two parallel but intertwined tasks: (1) a survey of Ugandan medical facilities to assess core components of anesthesia capacity, including workforce and (2) a mathematical model of anesthesia workforce which includes potential policy options to increase the number and/or quality of providers. 
- Aims (for model/paper):
	- Describe the flow of anesthetist training and employment in Uganda (AO, MMed, BSc Anes)
	- Describe the number, distribution, and characteristics of current anesthesia providers
	- Describe the estimated met and unmet demands for anesthesia services, as well as the the health effects (QALYs) of unmet demands 
	- Estimate the future number and distribution of anesthetists (ie, 2018-2050)
	- Estimate the effects of increasing the number of enrollees, improving retention, or increasing the number of positions for anesthesia providers in terms of number of practicing providers, ratio of providers to population, number of surgeries, and/or health benefits (ie, QALYs saved)
- Data Requirements
	- Number of anesthesiologist, AO anesthetists, other anesthesia providers, their distribution across facilities/regions at different points in time
	- Number of enrollees at training facilities, graduation rate, direct attrition to non-clinical positions, drop-out rate
	- Cost of training at each training level (faculty time, facilities, room/board, materials)
- Issues
	- Data availability: Unclear which of above are available
		- Items requiring primary data collection:
			- Attrition to non-clinical positions, non-anesthesia positions, and emmigration
			- Geographic distribution (how valuable is this vs. effort?)
- Methodology/technology: Computational speed should not be an issue. Developing the model in python might be easiest, but limits collaboration and/or future model use/development. Excel is likely the most accessible, and can accomplish all needed goals.  
- Plan
	- Meeting Jan 4th
	- Early-mid Jan: 
		- Tyler/Jim/Mike review document, advise Alex on data sources
		- Alex builds workflow diagram, collects data, more planning, review with Ugandan colleagues
	- Mid-Jan to Feb
		- Continue 
		- Initial model designed with real data where possible
		- Draft paper outline complete, fake figures, sections where relevant
	- Feb: Cardiology
	- March: 
		- Complete model, paper


# Jim’s comments 1/4/18

- Initial broad comments:
	1) Be clear about first priority, since your time is limited. Is it the model or the hospital survey? I think the model, with the data collection on anesthesia needs initially done informally via a focus group and potentially later (once you have the FG results and a functioning model) expanded to a real survey of hospitals. I.e., develop a solid version 1.0 of the model, to be improved with better parameterization over time.
	2) Do your best to estimate the effects of anesthesia staffing shortages, e.g., some combination of (a) non-performed or delayed surgeries and (b) surgeries out of practice scope for the anesthesiologist (eg low or very low cadre). Test wide by plausible ranges for these effects. I.e., "if 20% of surgeries for conditions [A, B, C] are cancelled and never done, the effect on DALYs is ..."
	3) consider excel then web-available as Google sheets, as we've been discussing for another project.


# Notes from early 2018 discussion: 

- Modeling CEA Non-physician anesthesia provider scale-up
	- Need to define the comparator
	- frequency of adverse events between cadres is unknown. In the US it is assumed to be similar more or less; in LICs it is assumed to be very different, though data are lacking
	- for the paper we’d assume no increase in adverse events - such a statement would require us to likely speculate about potential scopes of practice (i.e. those with 1yr training have not difference in outcomes when only doing C-sections and hernias). Bring data to bear on relative frequency of adverse events due to introduction of lower-level staff in other clinical areas and/or other countries, as necessary.  (See Next steps)
	- Need to account for cost savings potentially in terms of costs associated with physicians that could be avoided
	- could compare to no anesthesia provider at all (i.e. case doesn’t get done, or anesthesia mortality 1:100 like Togo nurse data - https://www.ncbi.nlm.nih.gov/pubmed/16354475 )
- Next Steps
	- Review data from other task sharing initiatives (surgery) where outcomes between higher and lower trained staff are measured and compared.
	- Obtain data on cost of training for different cadres (can get info for the AOs and the MMeds in Uganda and estimate for the new BSc that hasn’t yet started; could try to get other data from other countries)
	- Need info on the cost of surgery in Uganda and other countries (is it billed differently if an AO vs MMed provides anesthesia?)


# Notes (unknown date)
- Survey already administered at 13 sites - have the results
- Funding to expand to more sites
- Context: Lancet commission
- 2 anes residency
- Handful of non-MD training
- Cost bit
- Does mix or total matter more? Shortfall from what you need. Ie if 1000 providers needed, would 400 non-MDs or 300 MDs better?
- Global surgeries that didn’t happen - in the lancet commission
- Hypothetical: Room for hypothetical ideas - if 5% are high-risk, how does lack of anesthesia or MD effect outcome? 
- Hypothetical: How does # of surgeries and timing of surgeries effect outcome
- Log book to inform 
- Maybe Discrete choice experiments around:
- Housing packages
- Conditions/equipment
- Payment
- This job or that job - avoid social desirability bias
- There is a rural retention of COs DCE





# import re, string, unicodedata
# import nltk
# import contractions
# import inflect
# from bs4 import BeautifulSoup
# from nltk import word_tokenize, sent_tokenize
# from nltk.corpus import stopwords
# from nltk.stem import LancasterStemmer, WordNetLemmatizer

from nltk.corpus import wordnet
# from nltk.corpus import brown
# brown_ic = brown.raw('cj01.dat')
from nltk.corpus import wordnet_ic

brown_ic = wordnet_ic.ic('ic-brown.dat')
# vq_words = ["define" , "describe" ];
# l1= ["collect", "read", "speak" , "communicate" , "inform" , "identify" ,"comprehend"]
# l2 =["classify", "distinguish","explain"]
# l3 =["choose", "generalize","organize"]
# l4 =["classify", "analyse"]
# l5 =["criticize", "compare"]
# l6 =["combine", "construct","create"]

def res_sim_fun(vq_words=[]):
	l1=knowledge=['recite', 'review', 'point', 'recognize', 'describe', 'choose', 'examine', 'identify', 'enumerate', 'find', 'select', 'what', 'memorize', 'collect', 'sequence', 'when', 'duplicate', 'who', 'label', 'write', 'indicate', 'state', 'tabulate', 'which', 'relate', 'show', 'arrange', 'cite', 'match', 'define', 'locate', 'draw', 'repeat', 'remember', 'trace', 'read', 'quote', 'spell', 'memorise', 'how', 'observe', 'recognise', 'copy', 'why', 'outline', 'count', 'name', 'recall', 'study', 'omit', 'list', 'tell', 'reproduce', 'record', 'retell', 'meet', 'listen', 'where', 'order', 'view']

	l2=comprehension=['compare', 'cite', 'give', 'predict', 'recognize', 'describe', 'articulate', 'detail', 'order', 'characterize', 'generalize', 'factor', 'summarize', 'select', 'illustrate', 'visualize', 'group', 'trace', 'purpose', 'defend', 'rewrite', 'relate', 'approximate', 'demonstrate', 'indicate', 'add', 'interact', 'tell', 'extrapolate', 'show', 'rephrase', 'paraphrase', 'infer', 'contrast', 'locate', 'picture', 'extend', 'associate', 'conclude', 'express', 'interpolate', 'generalise', 'clarify', 'observe', 'understand', 'differentiate', 'review', 'distinguish', 'estimate', 'subtract', 'discuss', 'interpret', 'summarise', 'convert', 'translate', 'compute', 'outline', 'identify', 'elaborate', 'ask', 'example', 'classify', 'report', 'restate', 'explain', 'match']

	l3=application=['represent', 'show', 'identify', 'participate', 'derive', 'group', 'calculate', 'graph', 'dramatize', 'choose', 'factor', 'include', 'allocate', 'handle', 'practice', 'relate' 'schedule', 'report', 'assess', 'collect', 'investigate', 'categorise', 'ascertain', 'round', 'sketch', 'transcribe', 'sequence', 'imitate', 'discover', 'connect', 'tabulate', 'employ', 'avoid', 'experiment', 'manipulate', 'exercise', 'extend', 'associate', 'modify', 'personalize', 'dramatise', 'explore', 'teach', 'change', 'perform', 'summarise', 'act', 'implement', 'assign', 'alphabetize', 'relate', 'articulate', 'administer', 'subscribe', 'instruct', 'determine', 'apply', 'establish', 'select', 'illustrate', 'plot', 'use', 'prepare', 'paint', 'transfer', 'construct', 'process', 'interpret', 'translate', 'depreciate', 'complete', 'expose', 'acquire', 'adapt', 'link', 'simulate', 'diminish', 'compute', 'project', 'demonstrate', 'control', 'predict', 'contribute', 'examine', 'attain', 'capture', 'develop', 'provide', 'utilize', 'write', 'build', 'interview', 'organise', 'classify', 'draw', 'express', 'customize', 'price', 'chart', 'produce', 'plan', 'inform', 'solve', 'correlation', 'model', 'operate', 'convert']

	l4=analysis=['find', 'focus', 'identify', 'query', 'debate', 'relationships', 'derive', 'group', 'calculate', 'explain', 'theme', 'choose', 'reason', 'proof', 'reorganise', 'point', 'interrupt', 'difference', 'arrange', 'list', 'investigate', 'classify', 'discover', 'motive', 'deduce', 'connect', 'advertise', 'detect', 'confirm', 'research', 'experiment', 'size', 'cause', 'contrast', 'inspect', 'explore', 'distinguish', 'layout', 'optimize', 'interpret', 'question', 'omit', 'depth', 'ensure', 'distinction', 'inference', 'divide', 'relate', 'manage', 'rank', 'maximize', 'categorize', 'establish', 'select', 'illustrate', 'subdivide', 'transform', 'comparing', 'assumption', 'analyze', 'function', 'analyse', 'train', 'differentiate', 'breadboard', 'dissect', 'see', 'limit', 'highlight', 'appraise', 'diagnose', 'blueprint', 'compare', 'recognize', 'characterize', 'examine', 'file', 'discriminate', 'discussion', 'isolate', 'inventory', 'test', 'survey', 'document', 'infer', 'categorise', 'breakdown', 'separate', 'effect', 'diagram', 'simplify', 'point', 'audit', 'criticize', 'outline', 'correlate', 'minimize', 'prioritize', 'organise', 'model', 'order', 'test']

	l5=synthesis=['incorporate', 'code', 'reorganize', 'invent', 'generalize', 'compose', 'overhaul', 'explain', 'hypothesize', 'program', 'combine', 'choose', 'frame', 'integrate', 'collaborate', 'handle', 'format', 'propose', 'express', 'progress', 'reconstruct', 'speculate', 'discuss', 'comply', 'arrange', 'intervene', 'collect', 'hypothesise', 'debug', 'enhance', 'anticipate', 'originate', 'formulate', 'discover', 'reinforce', 'design', 'animate', 'substitute', 'network', 'join', 'experiment', 'adapt', 'lecture', 'contrast', 'extend', 'visualise', 'modify', 'makeup', 'prescribe', 'imagine', 'interface', 'estimate', 'generate', 'change', 'improve', 'convert', 'elaborate', 'initiate', 'individualize', 'think', 'revise', 'organize', 'relate', 'assemble', 'synthesize', 'categorize', 'summarize', 'prepare', 'create', 'transform', 'construct', 'predict', 'theorise', 'minimise', 'tell', 'cope', 'maximise', 'innovate', 'specify', 'communicate', 'setup', 'pretend', 'budget', 'compile', 'suppose', 'tabulate', 'delete', 'compare', 'rewrite', 'devise', 'abstract', 'dictate', 'cultivate', 'happen', 'portray', 'depict', 'develop', 'perform', 'make', 'write', 'build', 'test', 'negotiate', 'rearrange', 'simplify', 'produce', 'plan', 'validate', 'structure', 'add', 'outline', 'facilitate', 'correspond', 'solve', 'model', 'original']

	l6=evaluation=['validate', 'compare', 'deduct', 'useful', 'consider', 'conclude', 'predict', 'relate', 'describe', 'influence', 'rank', 'assess', 'rate', 'persuade', 'determine', 'measure', 'critique', 'mark', 'summarize', 'select', 'discuss', 'discriminate', 'prove', 'verify', 'defend', 'support', 'debate', 'grade', 'argue', 'disprove', 'recommend', 'test', 'infer', 'contrast', 'choose', 'attach', 'good', 'importance', 'evaluate', 'criteria', 'prescribe', 'hire', 'award', 'perceive', 'dispute', 'know', 'decide', 'opinion', 'judge', 'estimate', 'why', 'interpret', 'counsel', 'criticize', 'effective', 'prioritize', 'value', 'agree', 'bad', 'convince', 'prioritise', 'release', 'frame', 'appraise', 'explain', 'criticise', 'justify']

	cl_listoflist = []
	cl_listoflist.append(l1 )
	cl_listoflist.append(l2 )
	cl_listoflist.append(l3 )
	cl_listoflist.append(l4 )
	cl_listoflist.append(l5 )
	cl_listoflist.append(l6 )

	cnt_log=0

	final_level_of_ques=-1
	final_sim_of_ques_with_all_levels=[0, 0, 0, 0, 0, 0]
	final_area_sim_of_ques_with_all_levels=[0, 0, 0, 0, 0, 0]
	for vq_word in vq_words:
		# calculating sum and avg of sim of word with each list
		# print("\n\ndoing for word -----" , vq_word)
		sum_of_sim_all_levels = []
		avg_of_sim_all_levels = []
		for i ,list_i in enumerate(cl_listoflist):
			# print("list number  : " , i)
			sum_of_sim =0
			for l_word in list_i:
				# print("two words " , vq_word , l_word)
				if len(wordnet.synsets(vq_word))==0:
					# print vq_word
					break
				vq_word_syn=wordnet.synsets(vq_word)[0]
				# print("l_word => wordnet.synsets(l_word)",l_word, "=>" ,wordnet.synsets(l_word))
				if len(wordnet.synsets(l_word))==0:
					# print l_word
					continue
				l_word_syn=wordnet.synsets(l_word)[0]
				try:
					wup_sim=wordnet.res_similarity(vq_word_syn, l_word_syn, brown_ic)
				except:
					# print vq_word_syn,l_word_syn,"->exception"
					continue
				# wup_sim=(vq_word_syn).jcn_similarity(l_word_syn)
				if(type(wup_sim)!=type(None)):
					sum_of_sim = sum_of_sim + wup_sim
					# sum_of_sim += 1
					# print(" counted ",vq_word,l_word , "synset " , vq_word_syn , l_word_syn)
				else:
					cnt_log=cnt_log+1
					# print("Not counted             ",vq_word,l_word , "synset " , vq_word_syn , l_word_syn)
				# input()
			sum_of_sim_all_levels.append(sum_of_sim)
			avg_of_sim_all_levels.append( sum_of_sim / len(list_i) )


		# print("\n\n printing all lists")
		# for l in cl_listoflist:
		# 	print(l)

		# QUES WORK BEGIN
		# print ("Sim")
		for i in range(0,6):
			final_sim_of_ques_with_all_levels[i]+=avg_of_sim_all_levels[i]
		# 	print (final_sim_of_ques_with_all_levels[i],",")
		# print("\n")

		# print("area sim")
		for i in range(0,6):
			final_area_sim_of_ques_with_all_levels[i]+=sum_of_sim_all_levels[i]
		# 	print (final_area_sim_of_ques_with_all_levels[i],",")
		# print("\n")
		# print ("cnt_log",cnt_log)


	# print ("Final Sim")
	# for i in range(0,6):
	# 	print (final_sim_of_ques_with_all_levels[i],",")
	# print("\n")
	#
	# print ("Final Area Sim")
	# for i in range(0,6):
	# 	print (final_area_sim_of_ques_with_all_levels[i],",")
	# print("\n")

	#	maximum of all similarities values to find cl level
	final_level =0
	max_sim =final_sim_of_ques_with_all_levels[0]
	for index, sim in enumerate(final_sim_of_ques_with_all_levels):
		if sim  > max_sim :
			max_sim =sim
			final_level =index

	# print("\n")
	# print("avg wali list: " , avg_of_sim_all_levels)

	# print( "sum wali list: " , sum_of_sim_all_levels)

	# 	finding if word will be classified in  more than two levels
	count=0
	indices_of_same_sim=[]
	for i, sim in enumerate(final_sim_of_ques_with_all_levels):
		if sim==max_sim:
			count+=1
			indices_of_same_sim.append(i)

	# 	if word is in more than two levels
	if len (indices_of_same_sim)>1 :
		# print ("ques is in more than two levels")
		same_sim_list = []
		for index in indices_of_same_sim:
			same_sim_list.append(final_area_sim_of_ques_with_all_levels[index])

		max_sim_area =same_sim_list[0]
		for sim_area, index_of_max_sim in zip(same_sim_list ,indices_of_same_sim):
			if sim_area > max_sim_area:
				max_sim_area =sim_area
				final_level = index_of_max_sim

	# print("final_level ",final_level)
	return final_level

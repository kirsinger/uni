package com.nicta.biomed.bnst13.annotations;

import gov.nih.bnst13.preprocessing.combine.training.AnnotatedSentence;

import java.util.List;

public interface AnnotatedDocument {
	
	/** returns the doc id - eg 'PMC-423409806-05-Discussion' */
	public String getId();

	/** Return the list of annotated sentences of the document */
	public abstract List<? extends AnnotatedSentence> getAnnSentences();
	
	/** Return the ID of the last textual annotation which is a protein in the document */
	public int getLastProteinId();

}
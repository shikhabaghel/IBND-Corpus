# Indian-Broadcast-News-Debate-IBND-Corpus

The Indian Broadcast News Debate (IBND) corpus is created by collecting news debates from two popular English Indian news channels The corpus contains audio data of 15 TV news debates obtained from two Indian English news channels. The total duration of the corpus is 12 hours and 47 minutes. The corpus contains 94 unique speakers
(83 male and 11 female), excluding field reporters. The typical duration of each debate varies from 20 to 60 minutes. The IBND corpus consists of annotations for shouted, overlapped and competitive speech. The Praat phonetic software was used to perform the annotations. A total of 45 annotators were involved in the annotation
procedure of shouted and overlapped speech. Multiple annotators annotated each audio interval to minimize subjective bias. The statistics generated from
the final annotations indicate that there is significant presence of shouted, overlapped, and competitive speech in the IBND corpus. 

Audio data of the IBND corpus can not be shared due to copy right issues. However, different speech features extracted from IBND corpus along with annotations are available at the following Zenodo link

Zenodo Link: https://doi.org/10.5281/zenodo.8161172

More details of the corpus can be found in the paper (Link to the paper will be updated soon)  


# Audio Specifications
Sampling Rate: 16 kHz
Number of channels: 1

# Audio Features Description
Frame size: 25 ms
Frame shift: 10 ms

# Corpus Directory Structure
Directory structure of the corpus is as follows:




IBND_Corpus
          |----------> TVChannel_1
          |                    |------> ch1s1
          |                    |           |------> ch1s1d1
          |                    |                          |------> fetures
          |                    |                          |------> labels
          |                    |            |------> ch1s1d2
          |                    |                          |------> fetures
          |                    |                          |------> labels          
          |                    |                .
          |                    |                .
          |                    |                .
          |                    |------> ch1s2
          |                    |            |------> ch1s2d1
          |                    |                          |------> fetures
          |                    |                          |------> labels    
          |                    |            |------> ch1s2d2
          |                    |                          |------> fetures
          |                    |                          |------> labels    
          |                    |                .
          |                    |                .
          |                    |                .          
          |                    |------> ch1s3
          |                              .
          |                              .
          |                              .          
          |
          |
          |----------> TVChannel_2
                               |------> ch2s1
                               |           |------> ch2s1d1
                               |                          |------> fetures
                               |                          |------> labels
                               |            |------> ch2s1d2
                               |                          |------> fetures
                               |                          |------> labels          
                               |                .
                               |                .
                               |                .
                               |------> ch2s2
                                            |------> ch2s2d1
                                                          |------> fetures
                                                          |------> labels    
                                            |------> ch2s2d2
                                                          |------> fetures
                                                          |------> labels 
                                                .
                                                .
                                                .                                                          







          


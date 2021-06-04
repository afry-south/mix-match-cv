#### What task or questions did you try to solve?
Create a way to match a CV/resume to an assignment. Could simply be searching for keyword / experience.

#### What was challenges did you run into?
- Data collection
	- Finding good and somewhat structured resumes was difficult.
	- We did not get a very large dataset on assignments.
	- We did not have enough time for data cleaning/analysis.
- Labelling Data
- Processing data
- Imbalanced Data
- Multi word Keywords

Access to AFRYs database would help greatly.

#### Describe your conclusions and results?
Find a demo live [here](https://share.streamlit.io/afry-south/mix-match-cv/main/deployment.py).

- TfIdf works out pretty good.
- Clustering, KMeans
- Collecting data, vetting it, analyze it and potentially reiterate the process takes a lot of time
- Data Understanding should've been a larger step than it was, yet it was large enough to take time from modelling.

#### Is there a potential for further development?
- Structuring the data in the assignments, adding keywords, sections etc could generally be helpful when user skims/search assignments, but also for this use case.
- Gathering data on what Resume actually got an assignement would be very useful as labelled data.
     - Are we tying the assignment IDs to CVs today? I don't think so. You could write something like "I worked on assignment #<assignment-ID>" and create a a more data-robust mapping/relationship
- If access would be granted to AFRY resumes via e.g. an API then all data would a have a similar format which would help processing greatly.
- If at least some of the bullet points above could be crossed out, you could just make a better search algorithm and we would've already improved it quite a lot without any ML-driven searching/matching. ML is cool, though, and could improve it further.

#### How can we become better at innovation?
Innovation day is good but one day is not always enough to actually come up with and investigate a particular idea. If AFRY really believes in innovation it could be worth to allocate a full week for projects. An individual wanting to innovate is not always enough, you need to have time and possibly funding.
Other examples:
- Allocated time: N% Project: 3M, Google, Atlassian
- Spin-off/labs: Boston Dynamics, Amazon Kindle, loads of NASA spin-offs

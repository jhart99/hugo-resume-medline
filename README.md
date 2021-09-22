# hugo-resume-medline

This script takes a medline result file and converts the results into the markdown format used by [hugo-resume](https://github.com/eddiewebb/hugo-resume).  The medline results can be produced using [PubMed](https://pubmed.ncbi.nlm.nih.gov/) and choosing the save the results as "PubMed" format.  The results can also be taken from [SciENcv](https://www.ncbi.nlm.nih.gov/sciencv/) if you have already used that tool to generate an NIH biosketch for grant submission.

## Usage
### Prerequisites
* Python >3.7
* Biopython

### Command line
To generate templates for your publications download the Medline format results file and run the script on the results as shown:

    python3 parser.py medline.txt

This will generate a markdown file for each of your publications in a format suitable for further manual refinement.  The Tags are left unset because PubMed sets a *lot* of tags per publication.

To use these publications with hugo-resume, just copy the results to your content/publications directory.

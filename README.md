Installation

Clone the repository and set up your environment:

```bash
git clone https://github.com/navyarathore/ascii-image.git
cd ascii-image
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

uvicorn app.main:app --reload

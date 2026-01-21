# single-page-pdf-cutter
chop each page (potentially long) of a PDF into specified number of sections per page

## Usage 

### Install dependencies

```sh
pip install -r requirements.txt
```


### Run


```sh
python pagify_pdf.py <input_pdf> <output_pdf> [sections_per_page]
```

## Poster Chopper

Split a single-page poster PDF into a 3x3 grid (9 A4 pages) for printing on regular paper.

### Run

```sh
python title_poster.py <input_pdf> <output_pdf>
```

### Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `input_pdf` | No | Path to the input poster PDF (default: `poster.pdf`) |
| `output_pdf` | No | Path for the output PDF (default: `poster_9pages.pdf`) |

### Example

```sh
python title_poster.py my_poster.pdf my_poster_9pages.pdf
```
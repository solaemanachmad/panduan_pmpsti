# PMPSTI

## Tech Stack
- Quarto
- R (knitr engine)
- renv (environment management)

## Colors

- website background: #D9E3E4
- headings: #5B888C

## Contents
```bash
pmpsti/
├── front/
│   ├── editor.qmd
│   └── preface.qmd
│
├── chapter1/
│   ├── introduction.qmd
│   ├── images/
│   └── data/
│
├── chapter2/
│   ├── curricula.qmd
│   ├── images/
│   └── data/
│
├── chapter3/
│   ├── transition.qmd
│   ├── images/
│   └── data/
│
├── chapter4/
│   ├── conclusion.qmd
│   ├── images/
│   └── data/
│
├── appendix/
│   ├── appendix1.qmd
│   ├── appendix2.qmd
│   ├── ...
│   ├── images/
│   └── data/
│
├── index.qmd
└── _quarto.yml
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/solaemanachmad/panduan_pmpsti.git
cd panduan_pmpsti
```

### 2. Restore R Environment

Open R inside the project folder and run:

```r
renv::restore()
```

This will install all required packages based on `renv.lock`.

---

## Render Project

To render the full project:

```bash
quarto render
```

To preview locally:

```bash
quarto preview
```

---

## Notes

- All package versions are locked using `renv`
- Do not modify `renv.lock` manually
- Use branch-based workflow for major changes
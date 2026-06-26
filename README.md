    # Helmet Detection for Construction Site Safety

    **Author**: Seyi Akinduko, M.Sc Geophysics | PhD Applicant, ICON Lab, Monash University

    ## Overview
    This project is a v1 demo of computer vision for PPE compliance on construction sites. It uses YOLOv8 to detect `person` class from COCO.
    **Next step: V2 will fine-tune on a hard-hat dataset for true helmet vs no-helmet classification.**

    ## Tech Stack
    `Python` `YOLOv8` `OpenCV` `Ultralytics`

    ## How to Run
    ```bash
    pip install -r requirements.txt
    python detect.py --source 0 # Webcam
    python detect.py --source site.jpg # Image
    
## Research Relevance to ICON Lab
This work aligns with ICON Lab's focus on sensor analytics + computer vision for real-world systems. My background in Geophysics, ML, and embedded sensors supports building robust safety AI for construction.

## Roadmap
1. V1: COCO person detection baseline
2. V2: Fine-tune YOLOv8 on hard-hat dataset  
3. V3: Add no-helmet alerts + logging for compliance

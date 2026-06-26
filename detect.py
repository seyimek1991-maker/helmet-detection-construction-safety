    from ultralytics import YOLO
    import cv2
    import argparse

    def run_detection(source="0", conf=0.4):
        model = YOLO('yolov8n.pt')
        results = model.predict(source=source, conf=conf, classes=[0], stream=True, show=True)
        for r in results:
            cv2.imshow("Helmet Detection Demo - Press Q to quit", r.plot())
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        cv2.destroyAllWindows()

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--source", type=str, default="0")
        parser.add_argument("--conf", type=float, default=0.4)
        args = parser.parse_args()
        print(f" Starting. Source={args.source}")
        run_detection(source=args.source, conf=args.conf)

# Test commit for CI/CD workflow
# Test CI/CD trigger
# Trigger GitHub Actions

🚀 PROJECT: End-to-End ML App Deployment
📦 What You’ll Build
ML Model → Flask API → Docker Container → Render Cloud → GitHub Actions CI/CD

📂 PROJECT STRUCTURE
Create a folder:
ml-cloud-app/
│
├── train_model.py
├── model.pkl
├── app.py
├── requirements.txt
├── Dockerfile
└── .github/
    └── workflows/
        └── deploy.yml

🧠 STEP 1: Train the ML Model
- Load the Iris dataset.
- Train a RandomForest model.
- Save the trained model as model.pkl.
Run:
python train_model.py
✅ This generates the trained model file.

🌐 STEP 2: Create Flask API
- Build a Flask application.
- Load model.pkl.
- Create two endpoints:
    - /health → Returns app status
    - /predict → Accepts POST JSON input and returns prediction

Run locally:
python app.py

📄 STEP 3: Install Dependencies
Create requirements.txt and add:
- flask
- scikit-learn
- gunicorn
Install:
pip install -r requirements.txt

🧪 STEP 4: Test Locally
- Start the app:
python app.py

- Test prediction:
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d "{\"features\":[5.1,3.5,1.4,0.2]}"

- Expected output:
{"prediction":0}

🐳 STEP 5: Dockerize the Application
- Build image:
docker build -t ml-app .

- Run container:
docker run -p 5000:5000 ml-app

Test /predict again using curl.

☁️ STEP 6: Push Code to GitHub
git init
git add .
git commit -m "Initial commit"
git remote add origin <repo-url>
git push -u origin main

🚀 STEP 7: Deploy on Render
- Create a new Web Service.
- Connect GitHub repository.
- Select Docker runtime.
- Deploy.

🔎 HOW TO CHECK OUTPUT
✅ 1. Check Health Endpoint (Local)
Open browser:
http://127.0.0.1:5000/health

Output:
{"status":"ok"}

✅ 2. Check Prediction (Local)
Use curl:
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d "{\"features\":[5.1,3.5,1.4,0.2]}"

Output example:
{"prediction":0}

✅ 3. Check After Cloud Deployment
- Open in browser:
https://your-app.onrender.com/health

- If it shows:
{"status":"ok"}
✅ App is running successfully on cloud.

- Test prediction on cloud:
curl -X POST https://your-app.onrender.com/predict \
-H "Content-Type: application/json" \
-d "{\"features\":[5.1,3.5,1.4,0.2]}"

You will receive prediction output in JSON format.

🤖 STEP 8: Setup CI/CD
Create:
.github/workflows/deploy.yml

Configure it to:
- Trigger on push to main.
- Build Docker image automatically.
- Trigger redeployment.

Now whenever you run:
git push
✅ The application redeploys automatically.

OUTPUT IMAGES :-
1.
<img width="868" height="291" alt="Screenshot 2026-02-14 000431" src="https://github.com/user-attachments/assets/b707aec0-182a-4869-baf0-f3de173e1414" />
2.
<img width="907" height="356" alt="Screenshot 2026-02-14 001254" src="https://github.com/user-attachments/assets/dd1e3afd-d554-49b5-938b-ff1590fe4415" />
3.
<img width="1464" height="748" alt="Screenshot 2026-02-14 001606" src="https://github.com/user-attachments/assets/e7d4b65a-74ea-4382-b90e-57076a3b8883" />
4.
<img width="1134" height="298" alt="Screenshot 2026-02-14 002704" src="https://github.com/user-attachments/assets/1bcb0c2c-f7ba-42c6-bcf5-bd981c565e66" />
5.
<img width="1465" height="710" alt="Screenshot 2026-02-14 002739" src="https://github.com/user-attachments/assets/9d1067f1-1422-4201-aa42-8c8022da4a50" />
6.
<img width="1905" height="1072" alt="Screenshot 2026-02-14 003804" src="https://github.com/user-attachments/assets/e069f3be-0006-4b40-a09a-4f11b4173bcd" />
7.
<img width="1909" height="1085" alt="Screenshot 2026-02-14 003817" src="https://github.com/user-attachments/assets/1d98e665-0152-4038-a79e-910310002302" />
8.
<img width="1892" height="1072" alt="Screenshot 2026-02-14 121521" src="https://github.com/user-attachments/assets/ef77655c-6ace-4722-b1a9-9bb2f89899da" />
9.
<img width="1911" height="1031" alt="Screenshot 2026-02-14 121715" src="https://github.com/user-attachments/assets/3b860a24-0db3-49d8-9ba5-f91100b004cb" />
10.
<img width="1919" height="1013" alt="Screenshot 2026-02-14 121902" src="https://github.com/user-attachments/assets/e0f97431-c07c-4942-a0cc-0ee06983df53" />
11.
<img width="1038" height="294" alt="Screenshot 2026-02-14 122146" src="https://github.com/user-attachments/assets/47ce6297-902f-49df-9c24-c3da89c88757" />
12.
<img width="1910" height="1098" alt="Screenshot 2026-02-14 123315" src="https://github.com/user-attachments/assets/9a6f0e61-8890-4c3c-8722-9e574f0c2952" />
13.
<img width="1915" height="1088" alt="Screenshot 2026-02-14 123641" src="https://github.com/user-attachments/assets/65c005af-442d-4337-bfcf-ea11d16bef7f" />
14.
<img width="1903" height="1065" alt="Screenshot 2026-02-14 124527" src="https://github.com/user-attachments/assets/fe68cb05-2ad4-421c-982e-195093d0ba3e" />
15.
<img width="1882" height="1074" alt="Screenshot 2026-02-14 133403" src="https://github.com/user-attachments/assets/2a9eff73-34fc-493f-8d2b-b674aff969c5" />
16.
<img width="1912" height="1089" alt="Screenshot 2026-02-14 133424" src="https://github.com/user-attachments/assets/e9ad529b-4c6d-417a-9327-5814f8a74d69" />
17.
<img width="838" height="242" alt="Screenshot 2026-02-14 133546" src="https://github.com/user-attachments/assets/99cc5c22-8b30-4770-97cf-01b878d2f6dd" />
















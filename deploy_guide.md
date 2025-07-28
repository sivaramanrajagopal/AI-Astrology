# 🚀 Deployment Guide for AI Astrology App

## 📋 Prerequisites
- GitHub repository: `sivaramanrajagopal/AI-Astrology`
- OpenAI API Key: [Add your OpenAI API key in environment variables]

## 🔧 Render Backend Deployment

### Step 1: Create Render Web Service
1. Go to [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect GitHub repository: `sivaramanrajagopal/AI-Astrology`

### Step 2: Configure Service
```
Name: astro-backend
Environment: Python
Region: Choose closest to you
Branch: main
Root Directory: astro-backend
```

### Step 3: Build & Start Commands
```
Build Command: chmod +x build.sh && ./build.sh
Start Command: python start_minimal.py
```

### Step 4: Environment Variables
Add these in Render dashboard:
```
OPENAI_API_KEY=[Your OpenAI API Key]
ALLOWED_ORIGINS=https://ai-astrology.vercel.app
```

### Step 5: Advanced Settings
- Auto-Deploy: Yes
- Health Check Path: `/test`

## 🌐 Vercel Frontend Deployment

### Step 1: Create Vercel Project
1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import GitHub repository: `sivaramanrajagopal/AI-Astrology`

### Step 2: Configure Project
```
Framework Preset: Next.js
Root Directory: . (root)
Build Command: npm run build
Output Directory: .next
Install Command: npm install
```

### Step 3: Environment Variables
Add this in Vercel dashboard:
```
NEXT_PUBLIC_BACKEND_URL=https://your-render-backend-url.onrender.com
```
⚠️ Replace `your-render-backend-url` with your actual Render backend URL

### Step 4: Deploy Settings
- Production Branch: main
- Auto-Deploy: Yes

## ✅ Verification Steps

### Backend Verification
1. After Render deployment, test: `https://your-backend-url.onrender.com/test`
2. Should return: `{"status": "success", "message": "Server is running correctly!"}`

### Frontend Verification
1. After Vercel deployment, visit your Vercel URL
2. Should show the astrology app interface
3. Test the "🔧 Test Backend Connection" button

## 🔗 Final URLs
- Backend: `https://your-backend-url.onrender.com`
- Frontend: `https://ai-astrology.vercel.app`

## 🛠️ Troubleshooting

### If Backend Fails:
1. Check Render logs for Python/pyswisseph errors
2. Verify environment variables are set correctly
3. Ensure ephe files are present in astro-backend/ephe/

### If Frontend Fails:
1. Check Vercel logs for build errors
2. Verify NEXT_PUBLIC_BACKEND_URL is set correctly
3. Ensure all frontend files are in root directory

## 📞 Support
If you encounter issues, check:
1. Render deployment logs
2. Vercel deployment logs
3. Browser console for frontend errors
4. Network tab for API call failures 
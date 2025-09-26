# 🚀 Deployment Guide

## Deploy to Render.com

### Step 1: Push to GitHub

1. **Create a new repository on GitHub:**
   - Go to [github.com/new](https://github.com/new)
   - Repository name: `weather-math-assistant`
   - Make it public
   - Don't initialize with README (we already have one)

2. **Push your code:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/weather-math-assistant.git
   git push -u origin main
   ```

### Step 2: Deploy on Render

1. **Go to [render.com](https://render.com) and sign up/log in**

2. **Create a new Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select `weather-math-assistant`

3. **Configure the deployment:**
   - **Name:** `weather-math-assistant`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
   - **Instance Type:** `Free` (for testing)

4. **Environment Variables (Optional):**
   - Add `OPENWEATHER_API_KEY` if you want real weather data
   - Get free API key from [openweathermap.org/api](https://openweathermap.org/api)

5. **Deploy:**
   - Click "Create Web Service"
   - Wait 2-3 minutes for deployment
   - Your app will be live at `https://weather-math-assistant.onrender.com`

### Step 3: Test Your Deployment

✅ **Features that work without API keys:**
- Math calculations: "5 + 3", "calculate 15 * 7"
- Random math problems
- Word problems
- Expression parsing

✅ **Features that need OpenWeatherMap API key:**
- Weather queries: "weather in London"
- Temperature information

## 🎯 Quick Test Queries

Try these in your deployed app:

**Math Queries:**
- "Calculate 25 + 17"
- "What is 12 * 8?"
- "Give me a random math problem"

**Weather Queries:**
- "What's the weather in London?"
- "Temperature in New York"

## 🔧 Troubleshooting

**If deployment fails:**
1. Check the build logs in Render dashboard
2. Ensure `requirements.txt` has correct dependencies
3. Verify `Procfile` is present

**If math isn't working:**
- Check the console for JavaScript errors
- Math functions work offline, no API needed

**If weather isn't working:**
- Add `OPENWEATHER_API_KEY` environment variable
- Without API key, you'll get demo responses

## 💡 Pro Tips

1. **Free Render limits:**
   - App goes to sleep after 15 minutes of inactivity
   - First request after sleep takes ~30 seconds

2. **For production:**
   - Upgrade to paid plan for always-on hosting
   - Add custom domain in Render settings

3. **Monitoring:**
   - Check logs in Render dashboard
   - Set up health check endpoints if needed

## 🎉 You're Live!

Your Weather & Math Assistant is now deployed and accessible worldwide! 

Share your app URL with friends and showcase your full-stack development skills.

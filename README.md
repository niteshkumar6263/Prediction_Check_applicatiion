# Prediction Check Application

## Run the Streamlit frontend

Open PowerShell in the project folder and run:

```powershell
.\myenv\Scripts\Activate.ps1
streamlit run templates\home.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Integration status

The active frontend is `templates/home.py`.
It is directly connected to:

- `models/ridge.pkl`
- `models/scaler.pkl`

When you submit the form, Streamlit:

1. converts the selected class and region into numeric values
2. builds a dataframe in the correct feature order
3. scales the values with `scaler.pkl`
4. predicts FWI with `ridge.pkl`

## Notes

- `application.py` is a separate Flask app and is not the frontend you should run for this setup.
- If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
```

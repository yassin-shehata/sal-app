import pandas as pd
from openpyxl import load_workbook
import os

def append_or_create_excel(filename, sheet_name, data, headers):
    df_new = pd.DataFrame(data, columns=headers)

    if not os.path.isfile(filename):
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            df_new.to_excel(writer, index=False, sheet_name=sheet_name)
    else:
        book = load_workbook(filename)
        with pd.ExcelWriter(filename, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
            writer._book = book  # ✅ use _book instead of book
            if sheet_name in book.sheetnames:
                existing_df = pd.read_excel(filename, sheet_name=sheet_name)
                final_df = pd.concat([existing_df, df_new], ignore_index=True)
                final_df.to_excel(writer, index=False, sheet_name=sheet_name)
            else:
                df_new.to_excel(writer, index=False, sheet_name=sheet_name)

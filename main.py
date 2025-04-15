#!/usr/bin/env python3	
"""	
main.py	
	
This file orchestrates the overall workflow by calling the existing app.py logic	
and then the asynchronous API chain in match_data_fetch.py.	
It does not modify app.py logic.	
	
Ensure that app.py and match_data_fetch.py are in the same directory.	
"""	
	
from rich import print	
from app import main as app_main	
from match_data_fetch import fetch_match_ids, fetch_all_match_details	
import asyncio	
	
def main():	
    print("[bold green]Fetching match IDs from the primary endpoint...[/bold green]")	
    match_ids = fetch_match_ids()	
    if not match_ids:	
        print("[bold red]No match IDs fetched. Exiting.[/bold red]")	
        return	
	
    print(f"[bold cyan]Fetched match IDs: {match_ids}[/bold cyan]")	
	
    print("[bold green]Fetching detailed match data sequentially...[/bold green]")	
    detailed_data = asyncio.run(fetch_all_match_details(match_ids))	
	
    print("[bold cyan]Detailed match data fetched successfully.[/bold cyan]")	
    print(detailed_data) # Debug output to verify the fetched data	
	
if __name__ == "__main__":	
    main()
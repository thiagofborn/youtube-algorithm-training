import os
import random
import re
import time
from playwright.sync_api import sync_playwright

MAX_AZURE_VIDEO_AGE_DAYS = 1.5 * 365

def parse_relative_age_days(text):
    """Parse YouTube's relative upload date text (e.g. '3 months ago') into days."""
    m = re.search(r"(\d+)\s+(second|minute|hour|day|week|month|year)s?\s+ago", text or "", re.I)
    if not m:
        return None
    amount = int(m.group(1))
    unit_days = {
        "second": 1 / 86400, "minute": 1 / 1440, "hour": 1 / 24,
        "day": 1, "week": 7, "month": 30, "year": 365,
    }
    return amount * unit_days[m.group(2).lower()]

# Master matrix of top-tier engineering, systems, math, and science keywords
ALL_KEYWORDS = [
    # Enterprise Cloud Native & Multi-Cloud Architecture
    "Platform Engineering IDP Backstage Crossplane engineering",
    "Kubernetes multi-cluster GitOps ArgoCD advanced architecture",
    "AWS Karpenter EKS just-in-time compute scaling",
    "GKE Autopilot enterprise multi-tenancy security profiles",
    "Azure Private Link architecture with cross-tenant integration",
    "Multi-cloud hub-and-spoke transit gateway architecture AWS GCP Azure",
    "Zero Trust network architecture Zscaler integration enterprise cloud",
    "Cloud Native eBPF network observability Cilium advanced",
    "Policy-as-Code OPA Rego gatekeeper implementation CI CD",
    
    # Low-Level Systems & Programming
    "C programming strict aliasing and memory alignment optimization",
    "Linux kernel network stack internals eBPF tracing",
    "POSIX threads concurrency data race debugging C",
    "Win32 API memory mapped files asynchronous IO internals",
    "Unix systems programming signal handling IPC architecture",
    "Comprehensible input Polish native speaker listening",
    
    # Engineering Math & Computational Science
    "Queuing theory distributed systems capacity planning Little's Law",
    "Graph theory network topology routing optimization algorithms",
    "Linear algebra matrix decomposition distributed computing",
    "Discrete mathematics cryptography cryptographic primitives security",
    "Stochastic processes reliability engineering failure rate modeling",
    
    # Fundamental Chemistry, Energy & Materials
    "Lithium Iron Phosphate battery cell chemistry degradation mechanisms",
    "Semiconductor physics silicon doping lithography manufacturing chemical steps",
    "Thermodynamics of data center cooling fluid dynamics phase change",
    "Electrochemistry oxidation reduction reactions energy density profiles",
    "Materials science carbon intensity computation cycle analysis",
    "Permaculture zone 6 winter greenhouse Poland agriculture"
]

# Pick a dynamic, manageable subset of 5 random topics for this training session
TARGET_KEYWORDS = random.sample(ALL_KEYWORDS, 5)

def train_algorithm():
    with sync_playwright() as p:
        profile_path = os.path.abspath("playwright_youtube_profile")
        
        browser = p.chromium.launch_persistent_context(
            user_data_dir=profile_path,
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--start-maximized"
            ],
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        )
        
        page = browser.new_page()
        
        # Native stealth injection to mask automation flags
        page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        """)
        
        print("\n--> STARTING YOUTUBE INITIALIZATION...")
        page.goto("https://www.youtube.com")
        
        # Give the browser window time to fully open/render before proceeding
        wait_secs = 8
        print(f"\n[CHECK] If you are not logged in, please sign into Google in the browser window now.")
        print(f"--> Auto-continuing in {wait_secs}s (login persists via saved profile, so this is usually a no-op)...\n")
        page.wait_for_timeout(wait_secs * 1000)

        print(f"\n[STARTING RUN] Selected 5 random training vectors for this cycle.")
        
        for idx, keyword in enumerate(TARGET_KEYWORDS, start=1):
            print(f"\n--------------------------------------------------")
            print(f"Vector {idx}/5: Feeding keyword -> '{keyword}'")
            
            # Format query cleanly for URL execution
            encoded_query = keyword.replace(' ', '+')
            page.goto(f"https://www.youtube.com/results?search_query={encoded_query}")
            
            # Dynamic pause to mimic human skimming results page (3 to 6 seconds)
            page.wait_for_timeout(random.randint(3000, 6000))
            
            video_selector = "ytd-video-renderer"
            page.wait_for_selector(f"{video_selector} #video-title")
            videos = page.query_selector_all(video_selector)

            is_azure_topic = "azure" in keyword.lower()
            target = None
            for v in videos:
                title_el = v.query_selector("#video-title")
                if not title_el:
                    continue
                if is_azure_topic:
                    age_days = None
                    for span in v.query_selector_all("#metadata-line span"):
                        age_days = parse_relative_age_days(span.inner_text())
                        if age_days is not None:
                            break
                    if age_days is None or age_days > MAX_AZURE_VIDEO_AGE_DAYS:
                        continue
                target = title_el
                break

            if is_azure_topic and target is None:
                print("Warning: No Azure video within 1.5yr age limit found, skipping node.")
            elif target:
                # Target the top relevant result matching filters
                print("Targeting highest signal video asset...")
                target.click()
                
                # High-retention simulation: Choose a random watch time between 6 and 11 minutes
                watch_time_secs = random.randint(360, 660)
                print(f"Logging valued watch time context: {watch_time_secs // 60}m {watch_time_secs % 60}s...")
                
                # Sleep in short intermittent chunks to prevent script lock and mimic active focus
                elapsed = 0
                while elapsed < watch_time_secs:
                    time.sleep(10)
                    elapsed += 10
                    # Quick progress heartbeat
                    if elapsed % 120 == 0:
                        print(f"  -> Still watching... ({elapsed // 60}m elapsed)")
                        
                print(f"Target retention met for topic node.")
            else:
                print(f"Warning: No valid structural elements returned for this query node.")
                
            # Inter-video cool down break (4 to 8 seconds) to break machine-like looping signatures
            time.sleep(random.randint(4, 8))
            
        print("\n==================================================")
        print("TRAINING CYCLE COMPLETE. Feed weights updated successfully.")
        print("==================================================")
        browser.close()

if __name__ == "__main__":
    train_algorithm()
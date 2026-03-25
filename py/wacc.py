# WACC Teacher Program - Learn Weighted Average Cost of Capital Interactively!
# Enhanced with storytelling approach and better pacing

import time
import os

def clear_screen():
    """Clear terminal screen for better readability"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_section(title, delay=0.5):
    """Print a section with visual separation"""
    print("\n" + "═" * 70)
    print(f"✨ {title}")
    print("═" * 70)
    time.sleep(delay)

def typewriter(text, delay=0.03):
    """Typewriter effect for storytelling"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_positive_float(prompt):
    """Get positive float with validation"""
    while True:
        try:
            value = float(input(f"📊 {prompt}: "))
            if value < 0:
                print("❌ Please enter a positive number!")
                continue
            return value
        except ValueError:
            print("❌ Please enter a valid number!")

def print_progress_bar(iteration, total, length=50):
    """Show progress bar during calculations"""
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '░' * (length - filled_length)
    print(f'\rProgress: |{bar}| {percent}%', end='', flush=True)
    if iteration == total:
        print()

def main():
    while True:
        clear_screen()
        
        # ========== INTRODUCTION ==========
        print("\033[1;36m")  # Cyan color
        print_section("WACC TEACHER v2.0 - THE FINANCE STORYTELLER")
        print("\033[0m")  # Reset color
        
        typewriter("Hello! I'm your finance guide. Today, we're going to unravel...")
        time.sleep(0.5)
        
        print("\033[1;33m")  # Yellow color
        print("\n🎯 THE WEIGHTED AVERAGE COST OF CAPITAL (WACC)")
        print("\033[0m")
        
        time.sleep(1)
        typewriter("Think of WACC as the 'minimum return' a company needs to make.")
        time.sleep(0.5)
        typewriter("Like a hurdler who needs to clear a certain height...")
        time.sleep(0.5)
        typewriter("...a project needs to earn MORE than WACC to create value!")
        time.sleep(1)
        
        # ========== STORYTELLING: THE FORMULA ==========
        print_section("THE MAGIC FORMULA", delay=0.3)
        
        typewriter("Let me reveal the secret formula companies use:")
        print()
        
        # Animated formula reveal
        print("\033[1;35m")  # Magenta
        print("Step 1: Calculate total value...")
        time.sleep(0.3)
        print("    V = E + D")
        time.sleep(0.3)
        print("    (where E = Equity, D = Debt)")
        time.sleep(0.5)
        
        print("\nStep 2: Find the weights...")
        time.sleep(0.3)
        print("    We = E/V   (Equity weight)")
        time.sleep(0.3)
        print("    Wd = D/V   (Debt weight)")
        time.sleep(0.5)
        
        print("\nStep 3: The grand finale...")
        time.sleep(0.5)
        print("\033[1;32m")  # Green
        print("    ┌─────────────────────────────────────────────┐")
        print("    │  WACC = (We × Re) + (Wd × Rd × (1 - Tc))   │")
        print("    └─────────────────────────────────────────────┘")
        print("\033[0m")
        time.sleep(1)
        
        typewriter("\nWhere:")
        print("   Re = Cost of Equity (what shareholders expect)")
        print("   Rd = Cost of Debt (interest rate)")
        print("   Tc = Tax Rate (the government's 'discount' on debt!)")
        time.sleep(1)
        
        # ========== INTERACTIVE EXAMPLE ==========
        print_section("LET'S BUILD A COMPANY TOGETHER!", delay=0.3)
        
        typewriter("Imagine we're starting a company called 'TechNova Inc.'")
        time.sleep(0.5)
        typewriter("We need to decide: how should we finance it?")
        time.sleep(0.5)
        typewriter("Through shareholders (Equity) or through loans (Debt)?")
        time.sleep(1)
        
        print("\n\033[1;34m")  # Blue
        print("📈 CAPITAL STRUCTURE - Building our foundation")
        print("\033[0m")
        
        # Get inputs with storytelling
        print("\nFirst, let's value our company...")
        equity_value = get_positive_float("How much will shareholders invest? ($ millions)")
        debt_value = get_positive_float("How much will we borrow? ($ millions)")
        
        # Show calculation animation
        print("\nCalculating capital structure...")
        for i in range(101):
            print_progress_bar(i, 100)
            time.sleep(0.01)
        
        total_value = equity_value + debt_value
        weight_equity = equity_value / total_value
        weight_debt = debt_value / total_value
        
        print(f"\n✅ Total Company Value: ${total_value:,.1f} million")
        print(f"   → Equity portion: {weight_equity:.1%}")
        print(f"   → Debt portion:   {weight_debt:.1%}")
        time.sleep(1)
        
        # ========== COST OF CAPITAL ==========
        print("\n\033[1;34m")  # Blue
        print("💰 COST OF CAPITAL - What we pay our investors")
        print("\033[0m")
        
        typewriter("\nNow, what do our investors expect in return?")
        time.sleep(0.5)
        
        cost_equity = get_positive_float("What return do shareholders expect? (%)") / 100
        cost_debt = get_positive_float("What interest rate do banks charge? (%)") / 100
        tax_rate = get_positive_float("What's the corporate tax rate? (%)") / 100
        
        # Explain tax shield
        print("\n💡 Did you know? Interest on debt is tax-deductible!")
        time.sleep(0.5)
        print(f"   Without tax shield: Debt costs {cost_debt:.1%}")
        print(f"   With {tax_rate:.0%} tax rate: Debt costs only {cost_debt * (1 - tax_rate):.1%}")
        time.sleep(1)
        
        # ========== THE GRAND CALCULATION ==========
        print_section("THE BIG REVEAL - Calculating WACC", delay=0.3)
        
        print("\nLet me calculate TechNova's WACC...")
        time.sleep(0.5)
        
        # Animated calculation
        calculations = [
            ("Step 1: After-tax cost of debt", cost_debt * (1 - tax_rate)),
            ("Step 2: Equity contribution", weight_equity * cost_equity),
            ("Step 3: Debt contribution", weight_debt * cost_debt * (1 - tax_rate)),
        ]
        
        for step_name, value in calculations:
            print(f"\n{step_name}...")
            for i in range(101):
                print_progress_bar(i, 100)
                time.sleep(0.005)
            print(f"   → {value:.4%}")
            time.sleep(0.3)
        
        # Final WACC calculation
        wacc = (weight_equity * cost_equity) + (weight_debt * cost_debt * (1 - tax_rate))
        
        print("\n" + "⭐" * 70)
        print("\033[1;32m")  # Green
        print(f"🎉 TECHNOVA'S WACC = {wacc:.2%} 🎉")
        print("\033[0m")
        print("⭐" * 70)
        
        # ========== INTERPRETATION ==========
        print_section("WHAT DOES THIS MEAN?", delay=0.3)
        
        if wacc < 0.06:
            print("📊 Interpretation: Very low cost of capital!")
            print("   → TechNova is seen as very safe")
            print("   → Could mean it's a blue-chip company")
            print("   → Or maybe it has AAA credit rating")
        elif wacc > 0.12:
            print("📊 Interpretation: High cost of capital!")
            print("   → TechNova is seen as risky")
            print("   → Could be a startup or volatile industry")
            print("   → Investors demand higher returns")
        else:
            print("📊 Interpretation: Typical WACC range")
            print("   → TechNova is like most established companies")
            print("   → Balanced risk profile")
        
        time.sleep(1)
        
        print("\n💡 Key Insight: Any project TechNova undertakes...")
        print(f"   Must earn MORE than {wacc:.2%} to create value!")
        print(f"   If it earns LESS than {wacc:.2%}, value is destroyed.")
        time.sleep(1)
        
        # ========== SENSITIVITY ANALYSIS ==========
        print_section("WHAT IF...? (Sensitivity Analysis)", delay=0.3)
        
        print("\nLet's experiment! What if things change?")
        print("1. Try increasing debt - see the tax shield effect!")
        print("2. Try increasing risk - watch WACC rise!")
        print("3. Try changing tax rates - government policy matters!")
        
        time.sleep(0.5)
        
        change = input("\nWant to see what happens if Cost of Equity changes? (y/n): ").lower()
        if change == 'y':
            new_re = get_positive_float("New Cost of Equity (%)") / 100
            new_wacc = (weight_equity * new_re) + (weight_debt * cost_debt * (1 - tax_rate))
            diff = (new_wacc - wacc) * 100
            
            print(f"\n📈 New WACC: {new_wacc:.2%}")
            print(f"📉 Change: {diff:+.2f} percentage points")
            
            if diff > 0:
                print("→ TechNova just became more expensive to run!")
            else:
                print("→ TechNova just got cheaper to finance!")
        
        # ========== CONCLUSION ==========
        print_section("LESSONS LEARNED", delay=0.3)
        
        lessons = [
            "✓ WACC blends cost of equity and cost of debt",
            "✓ Debt has a tax advantage (tax shield!)",
            "✓ More debt lowers WACC... but increases risk",
            "✓ WACC is the 'hurdle rate' for investments",
            "✓ Every company has its own unique WACC"
        ]
        
        for lesson in lessons:
            print(lesson)
            time.sleep(0.3)
        
        # ========== PLAY AGAIN ==========
        print("\n" + "━" * 70)
        print("\033[1;36m")  # Cyan
        again = input("\nWant to build another company? (y/n): ").lower()
        print("\033[0m")
        
        if again != 'y':
            print("\n" + "💫" * 70)
            print("\nThanks for learning about WACC today!")
            print("Remember: Great investors understand the cost of capital!")
            print("\nKeep exploring finance! 🚀")
            print("\n" + "💫" * 70 + "\n")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for using WACC Teacher! Come back anytime!\n")

import matplotlib.pyplot as plt
import matplotlib

# Use a readable font family
matplotlib.rcParams['font.family'] = 'DejaVu Sans'

def generate_zero_trust_graph(df):
    plt.figure(figsize=(11, 6))
    bars = plt.bar(df['domain'], df['score'], color="#0d3b66")  # darker blue
    plt.xlabel('Security Domain', fontsize=14, fontweight='bold', color='white')
    plt.ylabel('Score', fontsize=14, fontweight='bold', color='white')
    plt.title('Zero Trust Posture', fontsize=16, fontweight='bold', color='white')
    plt.ylim(0, 100)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    ax = plt.gca()
    ax.set_facecolor('#1b1b1b')
    plt.gcf().patch.set_facecolor('#1b1b1b')

    plt.xticks(rotation=35, fontsize=11, color='white', ha='right')
    plt.yticks(fontsize=12, color='white')

    # Add value labels on top of bars with padding
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 2, f'{height}%', ha='center', color='white', fontsize=12)

    plt.tight_layout(rect=[0, 0.1, 1, 0.95])  # Add more bottom space for rotated labels
    plt.savefig('assets/graphs/zero_trust_posture.png', dpi=150, facecolor='#1b1b1b')
    plt.close()


def generate_iso_27001_graph(df):
    plt.figure(figsize=(11, 6))
    bars = plt.bar(df['control_id'], df['score'], color="#f4a261")  # softer orange
    plt.xlabel('ISO 27001 Control', fontsize=14, fontweight='bold', color='white')
    plt.ylabel('Compliance Score', fontsize=14, fontweight='bold', color='white')
    plt.title('ISO 27001 Control Coverage', fontsize=16, fontweight='bold', color='white')
    plt.ylim(0, 100)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    ax = plt.gca()
    ax.set_facecolor('#1b1b1b')
    plt.gcf().patch.set_facecolor('#1b1b1b')

    plt.xticks(rotation=35, fontsize=11, color='white', ha='right')
    plt.yticks(fontsize=12, color='white')

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 2, f'{height}%', ha='center', color='white', fontsize=12)

    plt.tight_layout(rect=[0, 0.1, 1, 0.95])
    plt.savefig('assets/graphs/iso_27001_coverage.png', dpi=150, facecolor='#1b1b1b')
    plt.close()

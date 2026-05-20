import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import date
from typing import List, Dict, Any
import io
import base64


def format_period_for_chart(period: date, grouping: str) -> str:
    if grouping == 'day':
        return period.strftime('%d.%m')
    else:
        return period.strftime('%m.%Y')


def create_inspections_count_chart(
        data: List[Dict[str, Any]],
        grouping: str,
        date_from: date,
        date_to: date,
) -> str:


    periods = []
    counts = []

    for item in data:
        period = item['period']
        count = item['count']

        period_label = format_period_for_chart(period, grouping)
        periods.append(period_label)
        counts.append(count)

    fig, ax = plt.subplots(figsize=(14, 6))

    bars = ax.bar(range(len(periods)), counts, color='steelblue', alpha=0.8)

    period_title = "дням" if grouping == 'day' else "месяцам"
    ax.set_xlabel('Период', fontsize=12)
    ax.set_ylabel('Количество проверок', fontsize=12)
    ax.set_title(
        f'Количество проверок за период с {date_from.strftime("%d.%m.%Y")} по {date_to.strftime("%d.%m.%Y")} (по {period_title})',
        fontsize=14)

    if grouping == 'day' and len(periods) > 15:
        plt.xticks(range(len(periods)), periods, rotation=45, ha='right', fontsize=8)
    elif grouping == 'day':
        plt.xticks(range(len(periods)), periods, rotation=45, ha='right', fontsize=10)
    else:
        plt.xticks(range(len(periods)), periods, rotation=0, fontsize=10)

    for i, (bar, count) in enumerate(zip(bars, counts)):
        if count > 0:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2., height + 0.5,
                    f'{count}', ha='center', va='bottom', fontsize=9)

    ax.grid(True, axis='y', alpha=0.3)
    ax.set_axisbelow(True)

    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode()
    plt.close()

    return image_base64
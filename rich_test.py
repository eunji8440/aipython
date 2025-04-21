# rich 라이브러리에서 필요한 기능들을 불러옵니다.
from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

# 1. 다양한 텍스트 스타일 출력
print("💡 [bold blue]Rich 스타일 출력 데모[/bold blue]")
print("반갑습니다! [green]파이썬[/green]으로 [bold]터미널 꾸미기[/bold] 시작해볼까요? :snake:")
print("[italic red]기울어진 빨간 글씨[/italic red]와 [underline yellow]밑줄 노란 글씨[/underline yellow]")
print("🎨 색상 조합: [reverse magenta on white]역상 강조 텍스트[/reverse magenta on white]")
print("=" * 50)

# 2. Panel 예제 - 정보 카드 스타일
print("\n📌 [bold cyan]패널 예시[/bold cyan]")
intro_text = Text()
intro_text.append("Rich는 ", style="white")
intro_text.append("터미널 UI", style="bold green")
intro_text.append("를 예쁘게 출력할 수 있게 해주는 라이브러리입니다. 🚀\n", style="white")
intro_text.append("Panel을 사용하면 정보를 카드처럼 표현할 수 있어요.", style="italic")

print(Panel(intro_text, title="[bold magenta]✨ 기능 소개 ✨[/bold magenta]", border_style="green", subtitle="powered by Rich", padding=(1, 2)))
print("=" * 50)

# 3. Table 예제 - 상태 테이블
print("\n📊 [bold yellow]상태 테이블 예시[/bold yellow]")

status_table = Table(title="서버 상태 모니터링", header_style="bold white on dark_green", show_lines=True)

status_table.add_column("서버 이름", style="cyan", no_wrap=True)
status_table.add_column("위치", style="blue")
status_table.add_column("상태", justify="center", style="bold")

status_table.add_row("Alpha", "서울", "[green]정상[/green]")
status_table.add_row("Beta", "부산", "[yellow]점검 중[/yellow]")
status_table.add_row("Gamma", "대전", "[red]오류 발생[/red]")

print(status_table)
print("=" * 50)

# 마무리 메시지
print("\n[bold underline green]Rich 덕분에 터미널이 살아났어요! 🌈[/bold underline green]")

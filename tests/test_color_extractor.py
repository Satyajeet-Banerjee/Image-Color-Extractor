from app.services.color_extractor import extract_top_colors

def test_color_extraction():
    colors = extract_top_colors("sample.jpg", k=5)
    assert len(colors) == 5
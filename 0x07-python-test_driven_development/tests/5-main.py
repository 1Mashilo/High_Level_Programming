
import unittest
from io import StringIO
import sys
from textwrap import dedent

module_name = "5-text_indentation"
text_indentation = __import__(module_name).text_indentation

class TestTextIndentation(unittest.TestCase):
    maxDiff = None  # Corrected placement of maxDiff attribute

    def setUp(self):
        self.capture_output = StringIO()
        sys.stdout = self.capture_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_text_indentation(self):
        input_text = dedent("""\
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
            Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
            Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
            Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
            Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
            rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
            stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
            cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
            beatiorem! Iam ruinas videres""")
        
        expected_output = dedent("""\
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            
            Quonam modo?
            Utrum igitur tibi litteram videor an totas paginas commovere?
            
            Non autem hoc:
            igitur ne illud quidem.
            Fortasse id optimum, sed ubi illud:
            Plus semper voluptatis?
            Teneo, inquit, finem illi videri nihil dolere.
            Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum
            rationi oboediens.
            Si id dicis, vicimus.
            Inde sermone vario sex illa a Dipylo
            stadia confecimus.
            Sin aliud quid voles, postea.
            Quae animi affectio suum
            cuique tribuens atque hanc, quam dico.
            Utinam quidem dicerent alium alio
            beatiorem!
            Iam ruinas videres
            """)

        text_indentation(input_text) 

        captured_output = self.capture_output.getvalue()
        self.assertEqual(captured_output, expected_output)

if __name__ == '__main__':
    unittest.main()

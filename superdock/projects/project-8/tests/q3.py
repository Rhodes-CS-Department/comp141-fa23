test = {
  'name': 'Question 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> read_ppm('images/simple.ppm')
          [[(255, 0, 0), (0, 255, 0)], [(0, 0, 255), (255, 0, 0)]]
          """,
          'hidden': False,
          'locked': False,
        },
        {
          'code': r"""
          >>> read_ppm('images/simple2.ppm')
          [[(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255)], [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)], [(255, 0, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0)], [(0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 0, 0)]]
          """,
          'hidden': False,
          'locked': False,
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

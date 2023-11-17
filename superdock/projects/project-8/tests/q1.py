test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> pixel_negate_red((86, 255, 24))
          (169, 255, 24)
          """,
          'hidden': False,
          'locked': False,
        },
        {
          'code': r"""
          >>> pixel_negate_green((58, 37, 105))
          (58, 218, 105)
          """,
          'hidden': False,
          'locked': False,
        },
        {
          'code': r"""
          >>> pixel_negate_blue((220, 118, 138))
          (220, 118, 117)
          """,
          'hidden': False,
          'locked': False,
        },
        {
          'code': r"""
          >>> pixel_negate_all((230, 61, 24))
          (25, 194, 231)
          """,
          'hidden': False,
          'locked': False,
        },
        {
          'code': r"""
          >>> pixel_remove_red((4, 170, 85))
          (0, 170, 85)
          """,
          'hidden': False,
          'locked': False,
        },
        {
          'code': r"""
          >>> pixel_remove_green((17, 173, 100))
          (17, 0, 100)
          """,
          'hidden': False,
          'locked': False,
        },
        {
          'code': r"""
          >>> pixel_remove_blue((16, 111, 59))
          (16, 111, 0)
          """,
          'hidden': False,
          'locked': False,
        },
        {
          'code': r"""
          >>> pixel_grayscale((11, 112, 255))
          (126, 126, 126)
          >>> pixel_grayscale((12, 112, 255))
          (126, 126, 126)
          >>> pixel_grayscale((13, 112, 255))
          (126, 126, 126)
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

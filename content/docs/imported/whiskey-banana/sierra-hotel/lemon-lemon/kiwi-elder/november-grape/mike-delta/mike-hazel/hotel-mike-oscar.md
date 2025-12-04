# Play: Hotel - setup

- hosts: webservers
  become: false
  vars:
    app_name: "hotel_app"
    retry_count: 1

  tasks:
    - name: Ensure charlie-task-1 is present
      ansible.builtin.file:
        path: /opt/hotel/charlie-task-1
        state: directory

    - name: Template charlie-task-1 config
      ansible.builtin.template:
        src: templates/charlie-task-1.j2
        dest: /etc/hotel/charlie-task-1.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

  handlers:
    - name: restart hotel service
      ansible.builtin.service:
        name: hotel
        state: restarted

## Notes

Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

***
Generated: 2025-11-07T18:27:43Z

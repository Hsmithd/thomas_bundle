# Play: Charlie - setup

- hosts: loadbalancers
  become: false
  vars:
    app_name: "charlie_app"
    retry_count: 5

  tasks:
    - name: Ensure hotel-task-1 is present
      ansible.builtin.file:
        path: /opt/charlie/hotel-task-1
        state: directory

    - name: Template hotel-task-1 config
      ansible.builtin.template:
        src: templates/hotel-task-1.j2
        dest: /etc/charlie/hotel-task-1.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure golf-task-2 is present
      ansible.builtin.file:
        path: /opt/charlie/golf-task-2
        state: directory

    - name: Template golf-task-2 config
      ansible.builtin.template:
        src: templates/golf-task-2.j2
        dest: /etc/charlie/golf-task-2.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure lima-task-3 is present
      ansible.builtin.file:
        path: /opt/charlie/lima-task-3
        state: directory

    - name: Template lima-task-3 config
      ansible.builtin.template:
        src: templates/lima-task-3.j2
        dest: /etc/charlie/lima-task-3.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

  handlers:
    - name: restart charlie service
      ansible.builtin.service:
        name: charlie
        state: restarted

## Notes

Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

***
Generated: 2025-11-07T18:27:43Z

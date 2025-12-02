# Play: Charlie - setup

- hosts: loadbalancers
  become: false
  vars:
    app_name: "charlie_app"
    retry_count: 2

  tasks:
    - name: Ensure delta-task-1 is present
      ansible.builtin.file:
        path: /opt/charlie/delta-task-1
        state: directory

    - name: Template delta-task-1 config
      ansible.builtin.template:
        src: templates/delta-task-1.j2
        dest: /etc/charlie/delta-task-1.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure cherry-task-2 is present
      ansible.builtin.file:
        path: /opt/charlie/cherry-task-2
        state: directory

    - name: Template cherry-task-2 config
      ansible.builtin.template:
        src: templates/cherry-task-2.j2
        dest: /etc/charlie/cherry-task-2.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

    - name: Ensure apple-task-3 is present
      ansible.builtin.file:
        path: /opt/charlie/apple-task-3
        state: directory

    - name: Template apple-task-3 config
      ansible.builtin.template:
        src: templates/apple-task-3.j2
        dest: /etc/charlie/apple-task-3.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure foxtrot-task-4 is present
      ansible.builtin.file:
        path: /opt/charlie/foxtrot-task-4
        state: directory

    - name: Template foxtrot-task-4 config
      ansible.builtin.template:
        src: templates/foxtrot-task-4.j2
        dest: /etc/charlie/foxtrot-task-4.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

  handlers:
    - name: restart charlie service
      ansible.builtin.service:
        name: charlie
        state: restarted

## Notes

Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

***
Generated: 2025-11-07T18:27:43Z
